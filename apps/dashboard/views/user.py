# DJANGO IMPORTS
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.base import File
from django.views.generic import View
from django.db.models import Q

# TOWI IMPORTS
from accounts.decorators import is_login, login_required
from accounts.models import (
    User, Center
)
from accounts.forms import EditAccountForm, CenterForm


ERROR = 40
SUCCESS = 25


class AccountInfo(View):
    @login_required
    def get(self, request):
        template_name = 'editar-info.html'
        ctx = {
            'user': request.user
        }
        return render(request, template_name, ctx)


class DataInformation(View):
    @login_required
    def get(self, request):
        editAccountForm = EditAccountForm(instance=request.user)
        if request.user.center:
            centerForm = CenterForm(instance=request.user.center)
        else:
            centerForm = CenterForm()
        template_name = 'admin-cuenta.html'
        ctx = {
            'editAccountForm': editAccountForm,
            'centerForm': centerForm
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request):
        data = request.POST
        action = data.get('action')
        if action == 'update_data':
            form = EditAccountForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    cd = form.cleaned_data
                    if cd['picture'] in [None, '']:
                        cd.pop('picture')
                    else:
                        request.user.picture = cd.pop('picture')
                        request.user.save()
                    User.objects.filter(pk=request.user.id).update(**cd)
                    messages.success(
                        request,
                        'Actualizaste con éxito tu perfil.'
                    )
                except Exception as e:
                    messages.error(
                        request,
                        'Ocurrio un error inesperado inténtalo mas tarde.'
                    )
            else:
                if form.errors:
                    for field in form:
                        for error in field.errors:
                            messages.add_message(request, ERROR, error)
                    centerForm = CenterForm(request.POST)
                    editAccountForm = EditAccountForm(instance=request.user)
                    template_name = 'admin-cuenta.html'
                    ctx = {
                        'editAccountForm': editAccountForm,
                        'centerForm': centerForm
                    }
                    return render(request, template_name, ctx)
        if 'save-center' in data:
            form = CenterForm(request.POST, request.FILES)
            if form.is_valid() and form.changed_data:
                cd = form.cleaned_data
                if request.user.center:
                    if request.user.center.name != cd['name']:
                        request.user.center.name = cd['name']
                    if cd['picture'] not in [None, '']:
                        request.user.center.picture = cd['picture']
                    request.user.center.save()
                else:
                    request.user.center = Center.objects.create(**cd)
                    request.user.save()
            else:
                if form.errors:
                    for field in form:
                        for error in field.errors:
                            messages.add_message(request, ERROR, error)
                    centerForm = CenterForm(request.POST)
                    editAccountForm = EditAccountForm(instance=request.user)
                    template_name = 'admin-cuenta.html'
                    ctx = {
                        'editAccountForm': editAccountForm,
                        'centerForm': centerForm
                    }
                    return render(request, template_name, ctx)
        return redirect('/cuenta')

    def validate_data(self, data, field):
        empty_list = ['', ' ', None]
        if data not in empty_list and data != field:
            return True
        else:
            return False
