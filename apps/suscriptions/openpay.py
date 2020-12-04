# STDLIB IMPORTS
import openpay

# DJANGO IMPORTS
from django.conf import settings

# APPLICATION IMPORTS
from .models import Order, SuscriptionType


class OpenPayManager(object):

    def __init__(self, *args, **kwargs):
        self.openpay = self._connection()
        self.monthly_sus = SuscriptionType.objects.filter(
            name='monthly'
        ).first() or 59
        self.quarterly_sus = SuscriptionType.objects.filter(
            name='quarterly'
        ).first() or 159

    def _connection(self):
        '''
        CONNECTION TO OPENPAY ACCOUNT
        '''
        openpay.verify_ssl_certs = False
        if settings.DEBUG is False:
            openpay.production = True
            openpay.api_key = settings.OPENPAY_API_KEY
            openpay.merchant_id = settings.OPENPAY_MERCHANT_ID
        else:
            openpay.api_key = settings.OPENPAY_API_KEY_SANDBOX
            openpay.merchant_id = settings.OPENPAY_MERCHANT_ID_SANDBOX
        return openpay

    def create_customer(self, user):
        '''
        METODO PARA REGISTRAR UN CLIENTE EN OPENPAY
        (UNO POR USUARIO, NO CAMBIAR SEGUN EL NOMBRE DE LA TARJETA)
        '''
        customer = self.openpay.Customer.create(
            name=user.first_name,
            email=user.email,
            last_name=user.last_name,
            phone_number=user.phone,
            requires_account=False
        )
        user.openpay_token = customer['id']
        user.save()

    def assign_card(self, token, user):
        '''
        METODO PARA ASIGNARLE UNA TARJETA A UN CUSTOMER
        '''
        pass

    def suscribe(self, plan, card, number_kids, order, user, amount):
        '''
        METODO PARA SUBSCRIBIR A UN CUSTOMER A UN PLAN
        EN ESTE CASO SOLO AL MENSUAL, CAMBIA SEGUN EL
        NUMERO DE NIÑOS
        '''
        customer = self.openpay.Customer.retrieve(user.openpay_token)
        if customer:
            try:
                response = customer.subscriptions.create(
                    plan_id=plan,
                    card_id=card,
                    order_id=order
                )                
                self.create_register(
                    amount,
                    number_kids,
                    'monthly',
                    user.id,
                    user.email,
                    order,
                    openpay_id=response.get('id')                   
                )
                return 200
            except openpay.error.CardError as error:
                return error.code
            except Exception as error:
                return 666

    def chargue(self, token, number_kids, description, dsi,
                order, user, option, amount):
        '''
        METODO PARA HACER UN CARGO NO RECURRENTE A UN CUSTOMER
        '''
        customer = self.openpay.Customer.retrieve(user.openpay_token)
        if customer:
            try:
                charge = customer.charges.create(
                    source_id=token,
                    method="card",
                    amount=amount,
                    description=description,
                    device_session_id=dsi,
                    order_id=order
                )                
                if charge.status == 'completed':
                    self.create_register(
                        amount,
                        number_kids,
                        option,
                        user.id,
                        user.email,
                        order,
                        openpay_id=charge.get('id')                
                    )
                    return 200
            except openpay.error.CardError as error:
                return error.code
            except Exception as error:
                return 666

    def create_register(self, amount, number_kids,
                        option, user_id, user_email, order, openpay_id):
        '''
        METODO QUE GUARDA UN REGISTRO DE LA COMPRA EN LA DB
        '''
        if option == 'monthly':
            price = self.monthly_sus.price
        else:
            price = self.quarterly_sus.price
        Order.objects.create(
            price=price,
            amount=amount,
            max_kids=int(number_kids),
            recurrency=option,
            user_id=user_id,
            user_email=user_email,
            open_pay_order_id=order,
            open_pay_id=openpay_id
        )
        return
    
    def cancel_suscription(self, user, subscription_id):
        '''
        METODO PARA CANCELAR SUSCRIPCIÓN MENSUAL Y RECURRENTE
        '''
        try:
            customer = self.openpay.Customer.retrieve(user.openpay_token)   
            subscriptions = customer.subscriptions.all()
            subscription = subscriptions.retrieve(subscription_id)
            subscription.delete()
            return 200
        except openpay.error.InvalidRequestError as error:
            return error
            

def get_suscription_id(number):
    '''
    IDS DE LOS PLANES CREADOS EN
    OPENPAY SEGUN EL NUMERO DE NIÑOS
    '''
    kids = int(number)
    if settings.DEBUG is True:
        return getattr(settings, 'OPENPAY_PLAN_{}_SANDBOX'.format(kids))
    else:
        return getattr(settings, 'OPENPAY_PLAN_{}'.format(kids))


def error_code_to_string(code):
    '''
    CODIGOS DE ERROR DE TARJETAS NO VALIDAS
    https://www.openpay.mx/docs/testing.html
    '''

    if code == 3001:
        return 'La tarjeta fue rechazada. Intenta con otra tarjeta'
    if code == 3002:
        return 'La tarjeta ha expirado.\
        Intenta con otra tarjeta'
    if code == 3003:
        return 'La tarjeta no tiene fondos suficientes.\
        Intenta con otra tarjeta'
    if code == 3004:
        return 'La tarjeta ha sido identificada como una tarjeta robada.\
        Intenta con otra tarjeta'
    if code == 3005:
        return 'La tarjeta ha sido rechazada por el sistema antifraudes.\
        Intenta con otra tarjeta'