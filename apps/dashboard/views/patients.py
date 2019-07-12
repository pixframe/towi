# STDLIB IMPORTS
from operator import attrgetter

# DJANGO CORE IMPORTS
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View

# TOWI IMPORTS
from accounts.decorators import login_required
from accounts.models import (
    User, Children,
    LinkedAccounts,
    LinkedAccountsChildrens
)
from suscriptions.openpay import OpenPayManager
from suscriptions.models import Order
from accounts.forms import ChildrenForm, AddPatientForm
from levels.models import Header, TowiIndex, ChildrenTowiIsland, Average, Quartile
from accounts.helpers import get_shared_childs, get_sharing_childs


ERROR = 40
SUCCESS = 25
INFO = 20


class Patients(View):
    @login_required
    def get(self, request):        
        template_name = 'pacientes.html'
        childrens = request.user.childrens.all()
        shared_childs = get_shared_childs(request.user)
        my_childs = get_sharing_childs(request.user)
        suscriptions = request.user.suscriptions.availables().count()
        ctx = {
            'user': request.user,
            'childrens': childrens,
            'shared_childs': shared_childs,
            'suscriptions_count': suscriptions
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request):
        if 'eliminarPaciente' in request.POST:
            try:
                child = Children.objects.get(
                    pk=request.POST['eliminarPaciente']
                )
                LinkedAccountsChildrens.objects.filter(cid=child).delete()
                child.status = 'deleted'
                child.save()
                child.suscription.remove_children()
                messages.add_message(request, SUCCESS, '¡Has eliminado al niño con éxito!')  # NOQA
                return redirect('/ninos')
            except Exception as e:
                messages.error(
                    request,
                    'No se pudo eliminar intente mas tarde.'
                )
                return redirect('/ninos')
        return redirect('/ninos')


class AddPatient(View):  # SOLO VIEW
    @login_required
    def get(self, request):
        template_name = 'agregarPaciente.html'
        user = request.user
        ctx = {
            'user': user,
            }
        return render(request, template_name, ctx)


class RegisterPatient(View):
    @login_required
    def get(self, request):
        template_name = 'registrarPaciente.html'
        form = ChildrenForm()
        user = request.user
        ctx = {
            'user': user,
            'form': form
            }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request):
        form = ChildrenForm(request.POST, request.FILES)
        list_options = request.POST.getlist('options')
        user = request.user
        suscriptions = request.user.suscriptions
        if not suscriptions.availables():
            messages.error(request, 'No tienes licencias disponibles.')
            return redirect('/ninos')
        if form.is_valid():
            cd = form.cleaned_data
            picture = cd.pop('picture')
            child = user.create_children(**cd)
            if picture is not None:
                child.picture = picture
            elif picture is None and list_options:
                child.picture = list_options[0]
            else:
                child.picture = 'avatars/girl-blue.png' if child.genre == 'Femenino' else 'avatars/boy-blue.png'  # NOQA
            child.save()
            child_suscription = suscriptions.availables().first()
            child_suscription.add_children(child)
            ChildrenTowiIsland.create_towi_island(user, child)
            messages.add_message(request, SUCCESS, 'Se agrego al niño con exito.')  # NOQA
            return redirect('/ninos')
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, ERROR, error)
            context = {
                'user': request.user,
                'form': ChildrenForm(request.POST)
            }
            return render(request, 'registrarPaciente.html', context)


class followPatient(View):
    @login_required
    def get(self, request):
        template_name = 'seguirPaciente.html'
        form = AddPatientForm()
        user = request.user
        ctx = {
            'user': user,
            'form': form
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request):
        if 'send-info' in request.POST:
            form = AddPatientForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                try:
                    user = User.objects.get(
                        email=cd['email'],
                        link_id=cd['link_id']
                    )
                    template_name = 'seguirPaciente.html'
                    ctx = {
                        'user': user.id,
                        'childs': user.get_active_childrens(),
                    }
                    return render(request, template_name, ctx)
                except User.DoesNotExist:
                    messages.add_message(request, ERROR, 'Usuario no encontrado, revisa la información.')  # NOQA
                    return redirect('/seguir')
        if 'send-child' in request.POST:
            owner_user = User.objects.get(pk=request.POST['owner_user'])
            children_id = request.POST['send-child']
            try:
                linked_account = LinkedAccounts.objects.get(
                    owner_user=owner_user,
                    shared_user=request.user
                )
            except LinkedAccounts.DoesNotExist as e:
                linked_account = LinkedAccounts.objects.create(
                    owner_user=owner_user,
                    shared_user=request.user
                )
            try:
                children = linked_account.childrens.get(cid__id=children_id)
            except LinkedAccountsChildrens.DoesNotExist:
                children = LinkedAccountsChildrens.objects.create(
                    linked_account=linked_account,
                    auth=True,
                    cid=Children.objects.get(pk=children_id)
                )
                messages.add_message(request, SUCCESS, 'Seguimiento exitoso.')  # NOQA
                return redirect('/ninos')
            if children.auth is True:
                messages.info(
                    request,
                    'Ya estas vinculado a este niño'
                )
            if children.auth is False:
                messages.info(
                    request,
                    'Ya te estan compartiendo a {}\
                    acepta la invitación'.format(
                        childre.cid.get_full_name
                    )
                )
            return redirect('/vinculaciones/')
        return redirect('/ninos')


class EditInfoPacient(View):
    @login_required
    def get(self, request, id):
        template_name = 'editar-info.html'
        try:
            child = request.user.childrens.get(pk=id)            
        except ObjectDoesNotExist as e:
            return redirect('/ninos/')
        form = ChildrenForm(instance=child)
        ctx = {
            'children': child,
            'user': request.user,
            'form': form
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request, id):
        form = ChildrenForm(request.POST, request.FILES)
        action = request.POST.get('action', None)
        options = request.POST.get('options', None)
        if 'eliminarPaciente' in request.POST:
            try:
                child = request.user.childrens.get(
                    pk=request.POST['eliminarPaciente']
                )
                LinkedAccountsChildrens.objects.filter(cid=child).delete()
                child.status = 'deleted'
                child.save()
                messages.add_message(request, SUCCESS, '¡Has eliminado al niño con éxito!')  # NOQA
                return redirect('/ninos/')

            except Exception as e:
                pass
        elif 'CancelSubscription' in request.POST:
            try:
                manager = OpenPayManager()
                user = request.user
                children = user.childrens.get(pk=id)
                children_suscription = children.suscription.order
                order = Order.objects.get(open_pay_order_id=children_suscription)
                subscription_id = order.open_pay_id
                cancel_subscription = manager.cancel_suscription(user, subscription_id)
                children.suscription.is_recurrent = False
                children.suscription.save()
                messages.add_message(request, SUCCESS, '¡Has cancelado la suscripción con éxito!')  # NOQA
                return redirect('/ninos/')   
            except Exception as e:
                messages.add_message(request, ERROR, '¡Algo inesperado ocurrio, vuelve a intentarlo más tarde!')  # NOQA
                return redirect('/ninos/')   
        elif action == 'update_child' and form.is_valid():
            cd = form.cleaned_data
            picture = cd.pop('picture')
            action = request.POST.get('action', None)
            options = request.POST.get('options', None)
            if action is not None:
                try:
                    if action == 'update_child':
                        if options:
                            picture = options
                        child = request.user.childrens.get(id=id)
                        child.first_name = cd['first_name']
                        child.last_name = cd['last_name']
                        if child.dob != cd['dob']:
                            child.dob = cd['dob']
                        child.grade = cd['grade']
                        child.genre = cd['genre']
                        child.diagnostic = cd['diagnostic']
                        child.laterality = cd['laterality']
                        child.videogames_usage = cd['videogames_usage']
                        child.failed_grades = cd['failed_grades']
                        if picture is not None:
                            child.picture = picture
                        child.save()
                    messages.add_message(request, SUCCESS, '¡Has editado al usuario con éxito!')  # NOQA
                except Exception as e:
                    messages.add_message(request, ERROR, 'Ocurrio un error inesperado, intentalo mas tarde.')  # NOQA

        return redirect('/perfil/{}'.format(id))


class Reports(View):
    @login_required
    def get(self, request, id):
        template_name = 'reportes.html'        
        user = request.user
        try:
            child = user.childrens.get(pk=id)
            if child.genre is None or child.genre == '':
                messages.add_message(request, INFO, 'Para continuar, debes actualizar el genero del niño')                                 
                return redirect('/perfil/{}'.format(id))        
            shared_child = False
        except ObjectDoesNotExist:
            shared_child = True
            accounts = get_shared_childs(user)
            if accounts.filter(cid__id=id).exists():
                child = accounts.filter(cid__id=id).first().cid
            else:
                messages.error(
                    request,
                    'No tienes registrado ningun niño con ese ID'
                )
                return redirect('/ninos')
        instancias = Header.objects.filter(cid__id=id)
        pruebas = instancias.filter(
            gamekey='PruebaEcologica'
        ).order_by(
            '-date'
        )
        headers = instancias.exclude(gamekey='PruebaEcologica')
        result_list = sorted(
            headers,
            key=attrgetter('date'),
            reverse=False
        )
        dates = set(obj.date.date() for obj in result_list if obj.date)
        days_list = []        
        count = 0        
        for date in dates:
            count += 1
            games = sorted(
                headers.filter(date__startswith=date),
                key=attrgetter('date', 'gamekey'),
                reverse=True
            )
            days_list.append(DaySession(
                date,
                games,
                count
                )
            )
        days_list.sort(key=lambda r: r.date, reverse=True)
        paginator = Paginator(days_list, 5)
        page = request.GET.get('page')
        try:
            days = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            days = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results
            days = paginator.page(paginator.num_pages)  
        ctx = {
            'children': child,
            'user': user,
            'days': days,
            'pruebas': pruebas,
            'shared_child': shared_child,
        }
        return render(request, template_name, ctx)


def get_graph(request):
    from django.http import JsonResponse
    child_id = request.GET.get('child_id', None)
    towiIndex = TowiIndex.objects.filter(cid=Children.objects.get(pk=child_id))
    labels = [ti.date.date().strftime("%s") for ti in towiIndex.order_by('-date')]  # NOQA
    if not labels:
        labels = [0, 0]
    maxValue = labels[0]
    minValue = labels[-1]

    am_ti = [{'x': str(ti.date.date().strftime("%s")), 'y': int(ti.index)} for ti in towiIndex.filter(  # NOQA
        cid=child_id,
        gamekey='ArbolMusical'
    ).order_by('date')]
    arm_ti = [{'x': str(ti.date.date().strftime("%s")), 'y': int(ti.index)} for ti in towiIndex.filter(  # NOQA
        cid=child_id,
        gamekey='ArenaMagica'
    ).order_by('date')]
    dqlb_ti = [{'x': str(ti.date.date().strftime("%s")), 'y': int(ti.index)} for ti in towiIndex.filter(  # NOQA
        cid=child_id,
        gamekey='DondeQuedoLaBolita'
    ).order_by('date')]
    rdt_ti = [{'x': str(ti.date.date().strftime("%s")), 'y': int(ti.index)} for ti in towiIndex.filter(  # NOQA
        cid=child_id,
        gamekey='Tesoro'
    ).order_by('date')]
    rio_ti = [{'x': str(ti.date.date().strftime("%s")), 'y': int(ti.index)} for ti in towiIndex.filter(  # NOQA
        cid=child_id,
        gamekey='Rio'
    ).order_by('date')]
    sh_ti = [{'x': str(ti.date.date().strftime("%s")), 'y': int(ti.index)} for ti in towiIndex.filter(  # NOQA
        cid=child_id,
        gamekey='JuegoDeSombras'
    ).order_by('date')]

    data = {
        'am_ti': am_ti,
        'arm_ti': arm_ti,
        'dqlb_ti': dqlb_ti,
        'rdt_ti': rdt_ti,
        'rio_ti': rio_ti,
        'sh_ti': sh_ti,
        'maxValue': maxValue,
        'minValue': minValue,
        'success': True
    }
    return JsonResponse(data)


def reports_redirect(request, id):
    response = redirect('{}/pruebas/{}/'.format(settings.TOWI_URL_REPORTS, id))
    # token = generate_jwt(request.user)
    # response['token'] = token
    return response


class DaySession(object):
    def __init__(self, date, games, count):
        self.date = date
        self.games = games
        self.count = count


class AssesmentView(View):
    def get(self, request, id):    
        template_name = 'assesment.html'        
        header = Header.objects.get(pk=id)
        if request.user.childrens.filter(pk=header.cid.id).exists():
            level = header.pruebaEcologica.first()
            age = header.cid.age
            if age < 6:
                age = 6
            elif age > 12:
                age = 12
            average = Average.objects.filter(age=age, gender=header.cid.genre).first()
            quartile = self.get_quartile_obj(header.cid, age, level)
            avg_quartile = self.get_average_quartile(quartile)
            ctx = dict(
                header=header,
                user=request.user,
                level=level,
                average=average,
                quartile=quartile,
                avg_quartile=avg_quartile
            )
            return render(request, template_name, ctx)
        else:
            messages.error(
                request,
                'No existe este niño en tu cuenta'
            )
            return redirect('/')
    
    def get_quartile_obj(self, children, age, level):        
        inverse = [
            'coins_extra_missed', 'flyplane_time',
            'flyplane_greenincorrect', 'flyplane_incorrect',
            'lab_hits_sum', 'lab_crosses_sum',
            'lab_deadends_sum', 'lab_time_sum', 'lab_latency_sum'
        ]
        quartile = dict()        
        objs = Quartile.objects.filter(age=age, gender=children.genre)
        quartile_one = objs.get(number=1)
        quartile_two = objs.get(number=2)
        quartile_three = objs.get(number=3)
        for field in Quartile._meta.fields:
            if field.attname not in ['age', 'gender', 'id', 'number']:
                field_name = field.attname
                value_1 = getattr(quartile_one, field_name)
                value_2 = getattr(quartile_two, field_name)
                value_3 = getattr(quartile_three, field_name)
                level_value = getattr(level, field_name)
                if level_value >= value_1:
                    if level_value >= value_2:
                        if level_value >= value_3:
                            quartile[field_name] = 4 if field_name not in inverse else 1
                        else:
                            quartile[field_name] = 3 if field_name not in inverse else 2
                    else:
                        quartile[field_name] = 2 if field_name not in inverse else 3
                else:
                    quartile[field_name] = 1 if field_name not in inverse else 4
        return quartile

    def get_average_quartile(self, quartile):
        avg_quartile = dict()
        atencion = ['coins_min_correct', 'coins_extra_missed']
        aprendizaje = ['arrange_total_correct', 'arrange_time']
        memoria = [
            'unpack_correct', 'packforward_score', 'packbackward_score',
            'waitroom_correct', 'flyplane_time'
        ]
        inhibicion = [
            'flyplane_greencorrect', 'flyplane_greenincorrect',
            'flyplane_correct', 'flyplane_incorrect'
        ]
        planeacion = [
            'lab_hits_sum', 'lab_crosses_sum', 'lab_deadends_sum'
        ]
        vel_process = ['lab_time_sum', 'lab_latency_sum']

        avg_quartile['atencion_avg'] = self.get_average([quartile.get(attr) for attr in atencion])
        avg_quartile['aprendizaje_avg'] = self.get_average([quartile.get(attr) for attr in aprendizaje])
        avg_quartile['memoria_avg'] = self.get_average([quartile.get(attr) for attr in memoria])
        avg_quartile['inhibicion_avg'] = self.get_average([quartile.get(attr) for attr in inhibicion])
        avg_quartile['planeacion_avg'] = self.get_average([quartile.get(attr) for attr in planeacion])
        avg_quartile['vel_process_avg'] = self.get_average([quartile.get(attr) for attr in vel_process])

        return avg_quartile

    def get_average(self, lst):
        return sum(lst) / len(lst)
