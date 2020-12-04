# STDLIB IMPORTS
from datetime import datetime

# DJANGO CORE IMPORTS
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse

# TOWI IMPORTS
from accounts.forms import RegisterLabForm, LoginForm
from accounts.models import User, Center
from accounts.decorators import login_required
from levels.models import (
    Prueba,
    ArbolMusical,
    ArenaMagica,
    RecoleccionTesoro,
    Sombras,
    Rio,
    DondeQuedoLaBolita,

    ArbolMusicalV2,
    ArenaMagicaV2,
    DondeQuedoLaBolitaV2,
    RecoleccionTesoroV2,
    RioV2,
    SombrasV2,
)
from levels.resources import *
from ..helpers import activity_to_english


ERROR = 40
SUCCESS = 25


class HomeLaboratorio(View):
    def get(self, request):
        template_name = 'ccl/index-lab.html'
        form = RegisterLabForm()
        loginForm = LoginForm()
        ctx = {
            'form': form,
            'loginForm': loginForm
        }
        return render(request, template_name, ctx)


class Tools(View):
    def get(self, request):
        template_name = 'ccl/tools.html'
        form = RegisterLabForm()
        loginForm = LoginForm()
        ctx = {
            'form': form,
            'loginForm': loginForm
        }
        return render(request, template_name, ctx)


class Researchers(View):
    def get(self, request):
        template_name = 'ccl/researchers.html'
        form = RegisterLabForm()
        loginForm = LoginForm()
        ctx = {
            'form': form,
            'loginForm': loginForm
        }
        return render(request, template_name, ctx)


class Projects(View):
    def get(self, request):
        template_name = 'ccl/projects.html'
        form = RegisterLabForm()
        loginForm = LoginForm()
        ctx = {
            'form': form,
            'loginForm': loginForm
        }
        return render(request, template_name, ctx)


class Resources(View):
    def get(self, request):
        template_name = 'ccl/resources.html'
        form = RegisterLabForm()
        loginForm = LoginForm()
        ctx = {
            'form': form,
            'loginForm': loginForm
        }
        return render(request, template_name, ctx)


class Participate(View):
    def get(self, request):
        template_name = 'ccl/participate.html'
        form = RegisterLabForm()
        loginForm = LoginForm()
        ctx = {
            'form': form,
            'loginForm': loginForm
        }
        return render(request, template_name, ctx)


class Data(View):
    def get(self, request):
        template_name = 'ccl/data.html'
        form = RegisterLabForm()
        loginForm = LoginForm()
        ctx = {
            'form': form,
            'loginForm': loginForm
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request):        
        NULL_VALUES = [None, 'all']
        if 'all-download' in request.POST:
            activity = request.POST.get('activity', None)
            school = request.POST.get('school', None)
            sex = request.POST.get('sex', None)
            grade = request.POST.get('grade', None)
            fro = request.POST.get('from', None)
            to = request.POST.get('to', None)
            qs = self.get_queryset()
            if school not in NULL_VALUES:
                qs = qs.filter(header__cid__school__type=school)
            if sex not in NULL_VALUES:
                qs = qs.filter(header__cid__genre=sex)
            if grade not in NULL_VALUES:
                if grade == 'Preschool':
                    qs = qs.filter(
                        Q(header__cid__grade='Kinder') |
                        Q(header__cid__grade='Preprimaria')
                    )
                else:
                    qs = qs.filter(header__cid__grade=grade)
            if request.POST['from'] and request.POST['to'] is not '':
                if request.POST['limit'] is not '':
                    limite = int(request.POST['limit'])
                    qs = qs.filter(
                        header__date__range=[fro, to]
                    )[:limite]
                else:
                    qs = qs.filter(
                        header__date__range=[fro, to]
                    )
            elif request.POST['limit'] is not '':
                limite = int(request.POST['limit'])
                qs = qs[:limite]
            else:
                qs = qs
            if not qs:
                messages.success(request, 'No data to download.')
                return redirect('.')
            dataset = self.get_dataset(qs, full=True)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="towi_kids_data_{}-{}.csv"'.format(activity_to_english(activity, full=True), datetime.now().date())  # NOQA
            return response
        if 'descargar' in request.POST:
            own_kids = False
            activity = request.POST.get('activity')
            qs = Prueba.objects.all().order_by('id')
            school = request.POST.get('school', None)
            sex = request.POST.get('sex', None)
            grade = request.POST.get('grade', None)
            fro = request.POST.get('from', None)
            to = request.POST.get('to', None)
            qs = self.get_queryset()
            if request.POST['kids'] == 'my':
                childs = request.user.childrens.all()
                qs = qs.filter(
                    header__cid__in=childs
                )
                own_kids = True
            if school not in NULL_VALUES:
                qs = qs.filter(header__cid__school__type=school)
            if sex not in NULL_VALUES:
                qs = qs.filter(header__cid__genre=sex)
            if grade not in NULL_VALUES:
                if grade == 'Preschool':
                    qs = qs.filter(
                        Q(header__cid__grade='Kinder') |
                        Q(header__cid__grade='Preprimaria')
                    )
                else:
                    qs = qs.filter(header__cid__grade=grade)
            if request.POST['from'] and request.POST['to'] is not '':
                if request.POST['limit'] is not '':
                    limite = int(request.POST['limit'])
                    qs = qs.filter(
                        header__date__range=[fro, to]
                    )[:limite]
                else:
                    qs = qs.filter(
                        header__date__range=[fro, to]
                    )
            elif request.POST['limit'] is not '':
                limite = int(request.POST['limit'])
                qs = qs[:limite]
            else:
                qs = qs
            if not qs:
                messages.success(request, 'No data to download.')
                return redirect('.')
            if own_kids is True:
                dataset = self.get_dataset(qs, full=True)
            else:
                dataset = self.get_dataset(qs, full=False)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="towi_kids_data_{}-{}.csv"'.format(activity_to_english(activity, full=False), datetime.now().date())  # NOQA
            return response

    def get_queryset(self):
        activity = self.request.POST.get('activity', None)
        if activity:
            if activity == 'PruebaEcologica':
                qs = Prueba.objects.all()
            elif activity == 'ArbolMusical':
                qs = ArbolMusicalV2.objects.all()
            elif activity == 'ArenaMagica':
                qs = ArenaMagicaV2.objects.all()
            elif activity == 'Rio':
                qs = RioV2.objects.all()
            elif activity == 'Tesoro':
                qs = RecoleccionTesoroV2.objects.all()
            elif activity == 'JuegoDeSombras':
                qs = SombrasV2.objects.all()
            elif activity == 'DondeQuedoLaBolita':
                qs = DondeQuedoLaBolitaV2.objects.all()
            else:
                qs = None
            return qs
        else:
            return None

    def get_dataset(self, queryset, full=False):
        activity = self.request.POST.get('activity', None)
        if activity:
            if activity == 'PruebaEcologica':
                if full is True:
                    dataset = PruebasFullResource().export(queryset)
                else:
                    dataset = PruebasDefaultResource().export(queryset)
            elif activity == 'ArbolMusical':
                if full is True:
                    dataset = ArbolMusicalFullResource().export(queryset)
                else:
                    dataset = ArbolMusicalLimitedResource().export(queryset)
            elif activity == 'ArenaMagica':
                if full is True:
                    dataset = ArenaMagicaFullResource().export(queryset)
                else:
                    dataset = ArenaMagicaLimitedResource().export(queryset)
            elif activity == 'Rio':
                if full is True:
                    dataset = RioFullResource().export(queryset)
                else:
                    dataset = RioLimitedResource().export(queryset)
            elif activity == 'Tesoro':
                if full is True:
                    dataset = RecoleccionTesoroFullResource().export(queryset)
                else:
                    dataset = RecoleccionTesoroLimitedResource().export(queryset)  # NOQA
            elif activity == 'JuegoDeSombras':
                if full is True:
                    dataset = SombrasFullResource().export(queryset)
                else:
                    dataset = SombrasLimitedResource().export(queryset)
            elif activity == 'DondeQuedoLaBolita':
                if full is True:
                    dataset = DondeQuedoLaBolitaFullResource().export(queryset)
                else:
                    dataset = DondeQuedoLaBolitaLimitedResource().export(queryset)  # NOQA
            else:
                dataset = None
            return dataset
        else:
            return None


def login_register(request):
    if request.method == 'POST':
        template_name = 'ccl/index-lab.html'
        data = request.POST
        action = request.POST['action']
        context = {
            'form': RegisterLabForm(),
            'loginForm': LoginForm()
        }
        if action == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                if user is None:
                    messages.error(request, 'Your email or password is incorrect, try again.')  # NOQA
                else:
                    login(request, user)
                    return redirect('/ccl/')
            else:
                if form.errors:
                    for field in form:
                        for error in field.errors:
                            messages.add_message(request, ERROR, error)
        elif action == 'registro':
            form = RegisterLabForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.create_user(**cd)
                user.researcher = True
                user.user_type = 'investigador'
                if 'center' in request.POST:
                    center = Center.objects.create(name=request.POST['center'])
                    user.center = center
                user.save()
                login(request, user)
                return redirect('/ccl/')
            else:
                if 'email' in form.errors:
                    if 'Ya existe' in form.errors['email'][0]:
                        user = authenticate(
                            username=form.data['email'],
                            password=form.data['password']
                        )
                        if user is None:
                            messages.error(
                                request,
                                'You already have a Towi account.'
                            )
                        else:
                            login(request, user)
                            return redirect('/ccl')
                else:
                    if form.errors:
                        for field in form:
                            for error in field.errors:
                                messages.add_message(request, ERROR, error)
            return render(request, template_name, context)
        return redirect('/')
