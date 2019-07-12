# STDLIB IMPORTS
import json

# DJANGO CORE IMPORTS
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned
from django.views.generic import View
from django.db.models import Q
from django.contrib import messages

# THIRD PARTY IMPORTS
from rest_framework_jwt.views import obtain_jwt_token

# TOWI IMPORTS
from accounts.decorators import is_login, login_required
from accounts.models import (
    User, UserType, Children, Group,
    LinkedAccounts,
    LinkedAccountsChildrens
)
from accounts.forms import InviteParentForm
from accounts.helpers import (
    get_sharing_childs,
    get_shared_childs,
    pending_approval_invitiations,
    pending_to_approve_invitiations,
)
from suscriptions.models import Suscription
from reusable.tasks import send_email
from reusable.sendgrid import EmailSendgrid


ERROR = 40
SUCCESS = 25


class InviteParent(View):
    @login_required
    def get(self, request, id):
        template_name = 'invitacion.html'
        form = InviteParentForm()
        child = request.user.childrens.get(pk=id)
        ctx = {
            'children': child,
            'user': request.user,
            'form': form
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request, id):
        form = InviteParentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            children = request.user.childrens.get(pk=id)
            try:
                user = User.objects.get(email=cd['email'])
                created_user = False
                msg = 'Vinculado con éxito, espera la confirmación.'
                email_name = 'seguimiento_existente'
            except User.DoesNotExist:
                user = User.objects.create_user(
                    **cd
                )
                Suscription.create_trial(user)
                created_user = True
                msg = 'Vinculado con éxito.'
                email_name = 'seguimiento_creada'
            try:
                linked_account = LinkedAccounts.objects.get(
                    owner_user=request.user,
                    shared_user=user
                )
            except LinkedAccounts.DoesNotExist:
                linked_account = LinkedAccounts.objects.create(
                    owner_user=request.user,
                    shared_user=user
                )
            try:
                children_la= linked_account.childrens.get(
                    cid=children
                )
                if children_la.auth is True:
                    messages.info(
                        request,
                        'Ya existe una vinculación de\
                        {} con {}.'.format(
                            children_la.cid.get_full_name,
                            user.email
                        )
                    )
                    return redirect('/ninos/')
                else:
                    messages.info(
                        request,
                        '{} aun no aprueba la invitación.'.format(
                            user.email
                        )
                    )
            except LinkedAccountsChildrens.DoesNotExist:
                LinkedAccountsChildrens.objects.create(
                    linked_account=linked_account,
                    cid=children,
                    auth=created_user
                )
                email_context = {
                    'email': user.email,
                    'children_name': children.get_full_name,
                    'name': user.display_name,
                    'sender_name': request.user.display_name
                }
                send_email.apply_async((email_name, email_context))
                messages.success(
                    request,
                    msg
                )
            return redirect('/vinculaciones/')
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, ERROR, error)
            form = InviteParentForm(request.POST)
            child = Children.objects.get(pk=id)
            ctx = {
                'children': child,
                'user': request.user,
                'form': form
            }
            return render(request, template_name, ctx)


class Invitations(View):
    @login_required
    def get(self, request):
        template_name = 'invitaciones.html'
        shared_pending = pending_approval_invitiations(request.user)
        shared_childs = get_shared_childs(request.user)
        my_childs = get_sharing_childs(request.user)
        owner_pending = pending_to_approve_invitiations(request.user)
        ctx = {
            'shared_pending': shared_pending,
            'shared_childs': shared_childs,
            'my_childs': my_childs,
            'owner_pending': owner_pending
        }
        return render(request, template_name, ctx)

    def post(self, request):
        data = request.POST
        if 'aceptar' in data:
            instance = LinkedAccountsChildrens.objects.get(
                pk=data['aceptar']
            )
            instance.auth = 1
            instance.save()
            messages.success(request, 'Invitación aceptada con éxito.')
            return redirect('/ninos')
        elif 'rechazar' in data:
            instance = LinkedAccountsChildrens.objects.get(
                pk=data['rechazar']
            )
            instance.delete()
            messages.success(request, 'Invitación rechazada con éxito.')
            return redirect('/ninos')
        elif 'desvincular' in data:
            instance = LinkedAccountsChildrens.objects.get(
                pk=data['desvincular']
            )
            instance.delete()
            messages.success(request, 'Desvinculación con éxito.')
            return redirect('/ninos')
        elif 'cancelar' in data:
            try:
                instance = LinkedAccountsChildrens.objects.get(
                    pk=data['cancelar']
                )
                instance.delete()
                messages.success(request, 'Se cancelo correctamente.')
                return redirect('/vinculaciones')
            except Exception as e:
                messages.error(
                    request,
                    'No se pudo cancelar la petición, intentalo mas tarde.'
                )
                return redirect('/vinculaciones')


class Seguimiento(View):
    @login_required
    def get(self, request):
        template_name = 'Seguimiento.html'
        childrens = request.user.childrens.all()
        ctx = {
            'user': request.user,
            'childrens': childrens,
            'vinculation_id': request.GET['id']
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request):
        ids = request.POST.getlist('id')
        data = request.POST
        if ids and 'vinid' in data:
            linked_o = LinkedAccountsChildrens.objects.get(pk=data['vinid'])
            linked_o.cid = int(ids.pop())
            linked_o.auth = 1
            linked_o.save()
            if ids:
                for id in ids:
                    LinkedAccountsChildrens.objects.create(
                        linked_account_id=linked_o.linked_account_id,
                        cid=id,
                        auth=1
                    )
                    messages.success(request, SUCCESS, '¡Vinculacion exitosa!')
                    return redirect('/vinculaciones')
            else:
                messages.success(request, SUCCESS, '¡Vinculacion exitosa!')
                return redirect('/vinculaciones')


def email_exists(request):
    from django.http import JsonResponse
    if request.method == 'GET':
        email = request.GET.get('email', None)
        data = {
            'is_taken': User.objects.filter(email=email).exists()
        }
        return JsonResponse(data)
    else:
        return None
