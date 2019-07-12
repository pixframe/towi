# STDLIB IMPORTS
import json

# DJANGO IMPORTS
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

# THIRD APPS
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# TOWI IMPORTS
from accounts.models import User
from .models import VerificationCode, Order, SuscriptionType


@swagger_auto_schema(method='post', auto_schema=None)
@api_view(['POST'])
def webhook(request):
    try:
        jsondata = request.body.decode('utf-8')
        hook = json.loads(jsondata)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    suscription_type = SuscriptionType.objects.filter(name='monthly').first()
    if hook['type'] == 'charge.succeeded':
        try:
            user = User.objects.get(openpay_token=hook['transaction']['id'])
            suscriptions = user.suscriptions.filter(
                order=hook['transaction']['order_id']
            )
            amount = hook['transaction']['amount']
            if suscription_type:
                number_kids = amount / suscription_type.price
            for suscription in suscriptions:
                suscription.update()
            try:
                Order.objects.create(
                    price=suscription_type.price,
                    max_kids=number_kids,
                    amount=amount,
                    recurrency='monthly',
                    user_id=user.id,
                    user_email=user.email,
                    created_date=timezone.now(),
                    open_pay_id=hook['transaction']['id'],
                    open_pay_order_id=hook['transaction']['order_id']
                )
            except Exception as e:
                pass
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if hook['type'] == 'verification':
        VerificationCode.objects.create(code=hook['verification_code'])
        return Response(status=status.HTTP_200_OK)
