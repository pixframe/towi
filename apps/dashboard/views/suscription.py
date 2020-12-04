# STDLIB IMPORTS
import hashlib
from datetime import timedelta

# DJANGO IMPORTS
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import View
from django.contrib.messages import get_messages
from django.utils import timezone
from django.conf import settings

# TOWI IMPORTS
from ..helpers import create_order_id
from accounts.decorators import is_login, login_required
from accounts.models import Children
from suscriptions.openpay import (
    OpenPayManager,
    get_suscription_id,
    error_code_to_string
)
from suscriptions.models import (
    SuscriptionType,
    Suscription,
    Order,
    Promos
)
from reusable.tasks import send_email


NULL_VALUE = [None, '']


class Licencias(View):
    @login_required
    def get(self, request):
        template_name = 'licencias.html'
        monthly = SuscriptionType.objects.get(name='monthly')
        quarterly = SuscriptionType.objects.get(name='quarterly')
        ctx = {
            'monthly_price': monthly.price,
            'quarterly_price': quarterly.price
        }
        return render(request, template_name, ctx)

    @login_required
    def post(self, request):
        kids_after_pay = request.POST.get('kids-suscription', None)
        suscription_choice = request.POST.get('suscription-choice', None)
        payment = request.POST.get('payment', None)
        if 'pre-code' in request.POST:
            try:
                promo = Promos.objects.get(promo_code=request.POST['pre-code'])  # NOQA
                price = promo.suscription.price
                amount = promo.amount
                total = price - amount
                if not total > 0:
                    if promo.unique is True:
                        promo.delete()
                    Suscription.create_new(
                        request.user,
                        promo.suscription.name,
                        is_recurrent=False
                    )
                    ctx = {
                        'childrens': request.user.get_inactive_childrens(),
                    }
                    try:
                        email_context = {
                            'name': request.user.display_name,
                            'email': request.user.email,
                        }
                        send_email.apply_async(('compra', email_context))
                        send_email.apply_async(('atencion', email_context))
                        send_email.apply_async(('formas_uso', email_context))
                    except Exception as e:
                        pass
                    messages.success(
                        request,
                        'Tu código prepago fue válido\
                        por una suscripcion {}'.format(
                            promo.suscription.get_name_display()
                        )
                    )
                    return render(request, 'pacientes_pago.html', ctx)
                else:
                    messages.info(
                        request,
                        'El código introducido es un descuento,\
                        utilizalo en el formulario de compra.'
                    )
                    return redirect('/subscripciones/')
            except Promos.DoesNotExist:
                messages.error(
                    request,
                    'El código prepago introducido no es válido.'
                )
                return redirect('/subscripciones/')

        if suscription_choice is not None:
            request.session['option'] = request.POST.get('option', None)
            request.session['number_kids'] = request.POST.get('kids-number', None)  # NOQA
            request.session['promo_code'] = request.POST.get('promo_code', None)  # NOQA
            suscription_type = SuscriptionType.objects.get(
                name=request.session['option']
            )
            amount = 0
            total = suscription_type.price * int(request.session['number_kids'])  # NOQA

            if request.session['promo_code'] not in NULL_VALUE:
                promo = suscription_type.has_promo(request.session['promo_code'])  # NOQA

                if promo:
                    amount = promo.amount
                    total = total - amount
                    if not total > 0:
                        if promo.unique is True:
                            promo.delete()
                        Suscription.create_new(
                            request.user,
                            suscription_type.name,
                            is_recurrent=False
                        )
                        ctx = {
                            'childrens': request.user.get_inactive_childrens(),
                        }
                        try:
                            email_context = {
                                'name': request.user.display_name,
                                'email': request.user.email,
                            }
                            send_email.apply_async(('compra', email_context))
                            send_email.apply_async(('atencion', email_context))
                            send_email.apply_async(('formas_uso', email_context))
                        except Exception as e:
                            pass
                        messages.success(
                            request,
                            'Tu cupon fue válido\
                            por una suscripcion {}'.format(
                                suscription_type.get_name_display()
                            )
                        )
                        return render(request, 'pacientes_pago.html', ctx)
                else:
                    messages.error(
                        request,
                        'El código promocional no es válido ó ya expiro.'
                    )
            request.session['amount'] = amount
            request.session['total'] = total
            ctx = {
                'PUBLIC_API_KEY': settings.OPENPAY_API_KEY_PUBLIC_SANDBOX if settings.DEBUG else settings.OPENPAY_API_KEY_PUBLIC,
                'ID_KEY': settings.OPENPAY_MERCHANT_ID_SANDBOX if settings.DEBUG else settings.OPENPAY_MERCHANT_ID
            }
            return render(request, 'pago.html', ctx)

        elif payment is not None:
            token_id = request.POST.get('token_id', None)
            dsi = request.POST.get('deviceIdHiddenFieldName', None)
            user = request.user
            suscription_type = request.session.get('option')
            number_kids = request.session.get('number_kids')
            promo_code = request.session.get('promo_code', None)
            order = create_order_id(user.id)
            request.session['order'] = order
            manager = OpenPayManager()
            suscription_type = SuscriptionType.objects.get(
                name=suscription_type
            )
            amount = (suscription_type.price * int(number_kids))
            description = 'Suscripcion {} para {} niños.'.format(
                suscription_type.get_name_display(),
                number_kids
            )
            if promo_code not in NULL_VALUE:
                promo_code = suscription_type.has_promo(promo_code)
                if promo_code:
                    amount -= promo_code.amount
                else:
                    messages.error(
                        request,
                        'El código promocional ya no es válido ó no es\
                        para esta subscripción. NO FUE APLICADO'
                    )

            if user.openpay_token in NULL_VALUE:
                try:
                    manager.create_customer(user)
                except Exception as e:
                    messages.error(
                        request,
                        'Ocurrio un error inesperado,\
                        intentalo más tarde. Codigo de error: 128MCC'
                    )
                    return redirect('/subscripciones/')
            if suscription_type.name == 'monthly' and promo_code in [False, None, '']:  # NOQA
                plan_id = get_suscription_id(number_kids)
                if plan_id:
                    code = manager.suscribe(
                        plan_id,
                        token_id,
                        number_kids,
                        order,
                        user,
                        amount
                    )
            elif suscription_type.name == 'quarterly' or promo_code:
                code = manager.chargue(
                    token_id,
                    number_kids,
                    description,
                    dsi,
                    order,
                    user,
                    suscription_type,
                    amount
                )
            if code is 200:
                if promo_code is True and promo.unique is True:
                    promo.delete()
                Suscription.create_new(
                    user,
                    suscription_type.name,
                    number_of_suscriptions=number_kids,
                    order=order,
                    is_recurrent=False if promo_code is True else True
                )
                email_context = {
                    'name': user.display_name,
                    'email': user.email,
                }
                send_email.apply_async(('compra', email_context))
                send_email.apply_async(('atencion', email_context))
                send_email.apply_async(('formas_uso', email_context))
                messages.success(
                    request,
                    'Gracias por tu compra, hemos actualizado tu cuenta.'
                )
                ctx = {
                    'childrens': request.user.get_inactive_childrens()
                }
                return render(request, 'pacientes_pago.html', ctx)
            else:
                messages.error(request, error_code_to_string(code))
                return render(request, 'pago.html')

        elif kids_after_pay is not None:
            user = request.user
            number_kids = int(request.session.pop('number_kids', 0))
            order = request.session.pop('order', None)
            childrens = request.POST.getlist('kids-selection', [])
            if childrens:
                for child in childrens:
                    child_sus = Suscription.objects.filter(
                        children__id=child
                    )
                    if child_sus.exists():
                        child_sus.delete()
                    sus = user.suscriptions.availables().filter(
                        order=order
                    ).first()
                    if sus:
                        sus.add_children(child)
                    else:
                        messages.error(
                            request,
                            'No tenias cuentas suficientes para activar\
                            a todos los niños seleccionados.'
                        )
                messages.success(
                    request,
                    'Hemos activado a los niños seleccionados.'
                )
                return redirect('/ninos')
            else:
                messages.success(
                    request,
                    '¡Ya tienes licencias disponibles, crea un perfil!'
                )
                return redirect('/ninos')
            return render(request, 'pago.html')
        else:
            return redirect('/subscripciones')


class ChildrenPago(View):
    def get(self, request):
        template_name = 'pacientes_pago.html'
        ctx = {
            'childrens': request.user.get_inactive_childrens()
        }
        return render(request, template_name, ctx)


class AssignSuscription(View):
    def get(self, request, id):
        template_name = 'assign_suscription.html'
        try:
            child = request.user.childrens.get(pk=id)
            suscriptions = request.user.suscriptions.availables()
            ctx = {
                'children': child,
                'monthly_count': suscriptions.filter(type__name='monthly').count(),  # NOQA
                'quarterly_count': suscriptions.filter(type__name='quarterly').count(),  # NOQA
                'monthly': suscriptions.filter(type__name='monthly').first(),
                'quarterly': suscriptions.filter(type__name='quarterly').first()  # NOQA
            }
            return render(request, template_name, ctx)
        except Children.DoesNotExist:
            messages.error(request, 'No tienes registrado a este niño')

    def post(self, request, id):
        try:
            children = request.user.childrens.get(pk=id)
            user = request.user
            _type = request.POST.get('option', None)
            suscription = user.suscriptions.availables().filter(
                type__name=_type
            ).first()
            if suscription:
                if suscription.objects.filter(user=user, children=children).exists():#agregue if aqui 04-11-2020
                    children.suscription.remove_children()
                suscription.add_children(children)
                messages.success(
                    request,
                    'Se asigno {} a una de tus subscripciones'.format(
                        children.get_full_name
                    )
                )
                return redirect('/ninos')
            else:
                messages.error(
                    request,
                    'Ya no tienes subscripciones {} disponibles'.format(_type)
                )
                return redirect('/ninos')
        except Children.DoesNotExist:
            messages.error(
                request,
                'Hubo un error con el niño, intente con otro'
            )
            return redirect('/ninos')


def coupon_exists(request):
    from django.http import JsonResponse
    if request.method == 'GET':
        coupon = request.GET.get('coupon', None)
        promo = Promos.objects.filter(promo_code=coupon)
        data = {
            'active': promo.exists(),
            'type': promo.first().suscription.get_name_display()
            if promo else None,
            'amount': promo.first().amount if promo else None
        }
        return JsonResponse(data)
    else:
        return None
