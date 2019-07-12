# DJANGO CORE IMPORTS
from django.shortcuts import (
    render,
    HttpResponseRedirect,
    redirect,
    HttpResponse
)
from django.contrib import messages
from django.views.generic import View
from django.db.models import Q

# TOWI IMPORTS
from accounts.decorators import is_login, login_required
from accounts.models import (
    User, UserType, Children, Group,
)

ERROR = 40
SUCCESS = 25


class Groups(View):
    @login_required
    def get(self, request):
        template_name = 'groups.html'
        groups = Group.objects.filter(user=request.user)
        childs = []
        for group in groups:
            for child in group.children.all():
                childs.append(child.id)
        children = Children.objects.filter(
            user=request.user).exclude(
                id__in=childs
            )
        context = {
            'groups': groups,
            'childs': children
        }
        return render(request, template_name, context)

    @login_required
    def post(self, request):
        data = request.POST
        if 'registro' in data:
            try:
                group = Group.objects.create(
                    user=request.user,
                    name=request.POST.get('name')
                )
            except Exception as e:
                pass
        elif 'modificacionNombreGrupo' in data:
            if 'groupName' in request.POST:
                try:
                    group = Group.objects.get(
                        id=data['modificacionNombreGrupo']
                    )
                    group.name = data['groupName']
                    group.save()
                    messages.add_message(request, SUCCESS, 'Se modifico el grupo con éxito.')  # NOQA
                    return redirect('/grupos')
                except Exception as e:
                    messages.add_message(request, ERROR, 'Ocurrio un error inesperado inténtalo mas tarde.')  # NOQA
                    return redirect('/grupos')

        elif 'eliminarGrupoButton' in data:
            try:
                group = Group.objects.get(id=data['eliminarGrupoButton'])
                group.delete()
                messages.add_message(request, SUCCESS, 'Se elimino el grupo con éxito,')  # NOQA
                return redirect('/grupos')
            except Exception as e:
                messages.add_message(request, ERROR, 'Ocurrio un error inesperado inténtalo mas tarde.')  # NOQA
                return redirect('/grupos')

        elif 'agregarPaciente' in data:
            try:
                group = Group.objects.get(id=data['agregarPaciente'])
                children = Children.objects.filter(
                    id__in=request.POST.getlist('options')
                )
                group.children.add(*children)
                group.save()
                messages.add_message(request, SUCCESS, 'Se agregaron los patients al grupo con éxito')  # NOQA
                return redirect('/grupos')
            except Exception as e:
                messages.add_message(request, ERROR, 'Ocurrio un error inesperado inténtalo mas tarde.')  # NOQA
                return redirect('/grupos')

        return HttpResponseRedirect('.')
