# STDLIB IMPORTS
from datetime import datetime, timedelta

# DJANGO CORE IMPORTS
from django.utils import timezone
from django.utils.timezone import make_aware
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

# THIRD PARTY IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics

# TOWI IMPORTS
from ...models import Promos, SuscriptionType, Suscription
from accounts.models import User
from ...helpers import get_finished_date
from .serializers import UserSuscriptionUpdateSerializer
from reusable.helpers import str_to_datetime


@api_view(['POST'])
def redeem_coupon(request):
    coupon = request.POST.get('code', None)
    user_id = request.POST.get('parent_id', None)
    child_id = request.POST.get('child_id', None)
    if coupon is not None:
        try:
            promo = Promos.objects.get(promo_code=coupon)
            user = User.objects.get(id=user_id)
            children_ids = []
            if child_id:
                child = user.childrens.filter(id=child_id).first()
            else:
                child = None
            if child:
                child.suscription.remove_children()
                children_ids = [child.id]
            Suscription.create_new(
                user,
                promo.suscription.name,
                ids=children_ids
            )
            if promo.unique is True:
                promo.delete()
            data = {
                'suscriptionsAvailables': user.suscriptions.availables().count()  # NOQA
            }
            return Response(data, status=status.HTTP_200_OK)
        except Promos.DoesNotExist as e:
            return Response(
                {
                    'status': 'COUPON_NOT_FOUND',
                    'message': 'The coupon does not exists'
                },
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist as e:
            return Response(
                {
                    'status': 'USER_NOT_FOUND',
                    'message': 'The user does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(
            {
                'status': 'ERROR',
                'message': 'Missing coupon parameter'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def suscription(request):
    try:
        number_kids = int(request.POST['number_kids'])
        parent_id = request.POST['parent_id']
        childrens = request.POST['childrens']
        type = request.POST['type']
        user = User.objects.get(pk=parent_id)
        suscription_type = SuscriptionType.objects.get(name=type)
        if childrens == '':
            childrens = []
        else:
            childrens = childrens.split(',')
        Suscription.create_new(
            user,
            suscription_type.name,
            ids=childrens,
            number_of_suscriptions=number_kids
        )
        return Response(
            {
                'status': 'Succesful',
                'suscriptionsAvailables': user.suscriptions.availables().count()  # NOQA
            }
        )
    except User.DoesNotExist as ue:
        return Response(
            {
                'status': 'USER_NOT_FOUND',
                'message': 'The user does not exists'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except SuscriptionType.DoesNotExist as se:
        return Response(
            {
                'status': 'SUSCRIPTION_TYPE_NOT_FOUND',
                'message': 'The type does not exists'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {
                'status': 'ERROR',
                'message': 'Missing parameters'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def active_child(request):
    try:
        cid_id = request.POST['child_id']
        parent_id = request.POST['parent_id']
        user = User.objects.get(pk=parent_id)
        children = user.childrens.get(pk=cid_id)
        suscription = user.suscriptions.availables().first()

        if suscription:
            children.suscription.remove_children()
            suscription.add_children(children)
            return Response(
                {
                    'status': 'Succesful',
                    'suscriptionsAvailables': user.suscriptions.availables().count()  # NOQA
                }
            )
        else:
            return Response(
                {
                    'status': 'ERROR',
                    'message': 'El usuario ya no tiene mas suscripciones'
                }
            )

    except User.DoesNotExist as u:
        return Response(
            {
                'status': 'USER_NOT_FOUND',
                'message': 'User not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except Children.DoesNotExist as c:
        return Response(
            {
                'status': 'USER_NOT_FOUND',
                'message': 'Children not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {
                'status': 'ERROR',
                'message': 'Missing parameters'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def update_user_suscription(request):
    try:
        parent_id = request.POST['parent_id']
        childrens = request.POST['childrens']
        str_date = request.POST['finished_date']
        finished_date = str_to_datetime(str_date)
        if finished_date is False:
            return Response(
                {
                  "error": {
                    "status": 400,
                    'message': 'Format must be %Y-%m-%dT%H:%M:%S'
                    }
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.get(pk=parent_id)
        ids = childrens.split(',')
        childrens = user.childrens.filter(id__in=ids)
        if childrens:
            for children in childrens:
                children.suscription.update(finished_date=finished_date)
            return Response(
                {
                  "succesful": {
                    "status": 200,
                    "message": "Subscription update"
                    }
                }
            )
        else:
            return Response(
                {
                  "error": {
                    "status": 404,
                    "message": "No childrens to update"
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )
    except User.DoesNotExist:
        return Response(
            {
              "error": {
                "status": 404,
                "message": "User not found"
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except MultiValueDictKeyError as e:
        return Response(
            {
              "error": {
                "status": 400,
                'message': 'Missing {} parameter'.format(e.args[0])
                }
            },
            status=status.HTTP_400_BAD_REQUEST
        )
