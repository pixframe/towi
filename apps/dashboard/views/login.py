# DJANGO CORE IMPORTS
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import View
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

# TOWI IMPORTS
from accounts.decorators import is_login, login_required
from accounts.models import User, UserType, Children
from accounts.forms import LoginForm, RegisterForm
from apps.accounts.tokens import account_activation_token
from levels.models import ChildrenTowiIsland
from suscriptions.models import Suscription
from reusable.tasks import (
    send_email,
    deactivate_childs,
)


REGISTRO = ['registro_familiar', 'registro_pacientes', 'registro_alumnos']
ERROR = 40
SUCCESS = 25
INFO = 20


class Home(View):
    @login_required
    def get(self, request):
        template_name = 'index.html'        
        return render(request, template_name)


class AboutTowi(View):
    @login_required
    def get(self, request):
        template_name = 'aboutTowi.html'
        return render(request, template_name)


class ActivateSent(View):
    def get(self, request, user_id):
        template_name = 'registration/email_confirmed.html'
        return render(request, template_name)
    
    def post(self, request, user_id):
        template_name = 'registration/email_confirmed.html'
        if 'send_email' in request.POST:
            user = User.objects.get(pk=user_id)
            current_site = get_current_site(request)
            email_context = {
                'email': user.email,
                'name': user.display_name,
                'protocol': request.scheme,
                'domain': current_site.domain,
                'uid': user.pk,
                'token': account_activation_token.make_token(user),
            }
            send_email.apply_async(('activation', email_context))
            messages.add_message(request, SUCCESS, '¡Correo enviado nuevamente!')
            return render(request, template_name)
        return render(request, template_name)


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = uidb64
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.confirmed_email = True
            user.save()
            children = user.childrens.first()
            if children is None:
                return redirect('/inicio')
            else:
                email_context = {
                    'email': user.email,
                    'name': user.display_name,
                    'children_name': children.first_name,
                }
                send_email.apply_async(('login', email_context))
                messages.add_message(request, INFO, '¡Confirmación exitosa!')
                login(request, user)               
                return redirect('/portal')
        else:
            # invalid link
            return render(request, 'registration/invalid_activation.html')


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/portal')
        template_name = 'login1.html'
        loginForm = LoginForm()
        registerForm = RegisterForm()
        context = {
            'form': loginForm,
            'registerForm': registerForm
        }
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'login1.html'
        data = request.POST
        action = request.POST['action']
        context = {
            'form': LoginForm(),
            'registerForm': RegisterForm()
        }
        if action == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )    
                if user is None:
                    messages.error(request, 'Tu correo ó contraseña son incorrectos, inténtalo de nuevo.')  # NOQA
                # elif user.confirmed_email is False:
                #     messages.error(request, 'Por favor verifica tu correo')  # NOQA
                #     return redirect('activation-sent', user.id)
                else:
                    login(request, user)
                    deactivate_childs.apply_async((user.id, ))
                    return redirect('/subscripciones/')
            else:
                if form.errors:
                    for field in form:
                        for error in field.errors:
                            messages.add_message(request, ERROR, error)
        elif action in REGISTRO:
            form = RegisterForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                dob = request.POST['year'] + '-' + request.POST['month'] + '-' + request.POST['day']
                picture = ''
                cd['child_dob'] = dob
                if action == 'registro_familiar':
                    user_type = 'familiar'
                    picture = 'avatars/male.png'
                elif action == 'registro_pacientes':
                    user_type = 'especialista'
                    picture = 'avatars/doctor-male.png'
                else:
                    user_type = 'escuela'
                    picture = 'avatars/boy-aquamarine.png'
                try:
                    user = User.objects.create_user(
                        first_name=cd['first_name'],
                        email=cd['email'],
                        password=cd['password'],
                        user_type=user_type,
                        picture=picture
                    )
                    children = user.create_children(
                        cd['child_name'],
                        cd['child_dob']
                    )
                    Suscription.create_trial(user, children)
                    ChildrenTowiIsland.create_towi_island(user, children)
                    current_site = get_current_site(request)
                    email_context = {
                        'email': user.email,
                        'name': user.display_name,
                        'protocol': request.scheme,
                        'domain': current_site.domain,
                        'uid': user.pk,
                        'token': account_activation_token.make_token(user),
                    }
                    send_email.apply_async(('activation', email_context))
                    login(request, user)
                    return redirect('/subscripciones/')
                except Exception as e:
                    if user:
                        user.delete()
                    messages.error(
                        request,
                        'Ocurrio un error inesperado inténtalo mas tarde.'
                    )
            else:
                template_name = 'login1.html'
                messages.error(
                    request,
                    'Ingresaste datos incorrectos, corrigelos.'
                )
                context = {
                    'registerForm': form,
                    'form': LoginForm()
                }
                return render(request, template_name, context)
        return render(request, template_name, context)
