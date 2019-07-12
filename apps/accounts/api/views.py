# STDLIB IMPORTS
import re
import json
from datetime import datetime, timedelta

# DJANGO CORE IMPORTS
from django.utils import timezone
from django.utils.timezone import make_aware
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q

# THIRD PARTY IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

# TOWI IMPORTS
from ..models import User, Children, FreeTrial, UserType
from ..helpers import deactivate_childrens
from .serializers import LoginSerializer, ProfilesSerializer
from levels.models import Session, ChildrenTowiIsland
from reusable.responses import *
from reusable.helpers import str_to_date, str_to_bool
from suscriptions.models import Suscription
from apps.accounts.tokens import account_activation_token
from reusable.tasks import send_email
from reusable.docs import *


@swagger_auto_schema(method='post', auto_schema=None)
@api_view(['POST'])
def login(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    if password is not None or email is not None:
        user = authenticate(username=email, password=password)
        if user is not None:
            deactivate_childrens(user.id)
            serializer = LoginSerializer(user)
            return Response(serializer.data)
        else:
            return Response(USER_NOT_FOUND, status=status.HTTP_401_UNAUTHORIZED)  # NOQA
    else:
        return Response(ERROR_MISSING_EMAIL_PASSWORD, status=status.HTTP_400_BAD_REQUEST)  # NOQA


@swagger_auto_schema(
    method='POST',
    operation_description="Endpoint that return the game data\
    of each child of the user.",
    operation_summary='api/sync_profiles',
    manual_parameters=[userkey_param],
    responses={
        200: ProfilesSerializer(many=True),
        404: 'USER_NOT_FOUND',
        400: 'ERROR_MISSING_USERKEY'
        }
)
@api_view(['POST'])
def sync_profiles(request):
    key = request.POST.get('userKey', None)
    if key is not None:
        try:
            user = User.objects.get(key=key)
            profiles = ProfilesSerializer(user.towiIsland.all(), many=True)
            return Response(profiles.data)
        except User.DoesNotExist:
            return Response(USER_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)  # NOQA
    return Response(ERROR_MISSING_USERKEY, status=status.HTTP_400_BAD_REQUEST)  # NOQA


@swagger_auto_schema(
    method='POST',
    operation_description="Endpoint to update the game data of a child.",
    operation_summary='api/update_profile',
    manual_parameters=[json_param],
    responses={
        200: "OK",
        404: 'USER_NOT_FOUND',
        400: 'ERROR_MISSING_JSON'
        }
)
@api_view(['POST'])
def update_profile(request):
    json_to_parse = request.POST.get('jsonToDb', None)
    parsed_json = json.loads(json_to_parse)
    if parsed_json is not None:
        try:
            user = User.objects.get(key=parsed_json.pop('userKey'))
            children = user.childrens.get(id=parsed_json['cid'])
            towi_island = children.towiIslandChild.all().first()
            towi_island.kiwis = parsed_json['kiwis']
            towi_island.avatar = parsed_json['avatar']
            towi_island.avatarclothes = parsed_json['avatarclothes']
            towi_island.owneditems = parsed_json['owneditems']
            towi_island.rio_first_time = parsed_json['rioFirstTime']
            towi_island.tesoro_first_time = str_to_bool(parsed_json['tesoroFirstTime'])  # NOQA
            towi_island.arbol_first_time = str_to_bool(parsed_json['arbolFirstTime'])  # NOQA
            towi_island.arena_first_time = str_to_bool(parsed_json['arenaFirstTime'])  # NOQA
            towi_island.sombras_first_time = str_to_bool(parsed_json['sombrasFirstTime'])  # NOQA
            towi_island.bolita_first_time = str_to_bool(parsed_json['bolitaFirstTime'])  # NOQA
            towi_island.rio_level_set = str_to_bool(parsed_json['rioLevelSet'])  # NOQA
            towi_island.tesoro_level_set = str_to_bool(parsed_json['tesoroLevelSet'])  # NOQA
            towi_island.arbol_level_set = str_to_bool(parsed_json['arbolLevelSet'])  # NOQA
            towi_island.arena_level_set = str_to_bool(parsed_json['arenaLevelSet'])  # NOQA
            towi_island.arena_level_set2 = str_to_bool(parsed_json['arenaLevelSet2'])  # NOQA
            towi_island.sombras_level_set = str_to_bool(parsed_json['sombrasLevelSet'])  # NOQA
            towi_island.bolita_level_set = str_to_bool(parsed_json['bolitaLevelSet'])  # NOQA
            towi_island.island_shopping_list = parsed_json['islandShoppingList']  # NOQA
            if children.suscription.trial is True and towi_island.first_time_completed() is True:  # NOQA
                children.suscription.trial = False
                children.suscription.save()
                email_context = {
                    'email': user.email,
                    'child_name': children.get_full_name,
                    'name': user.display_name
                }
                send_email.apply_async(('prueba_finalizada', email_context))            
            if parsed_json['activemissions']:
                active_missions = ", ".join(str(x) for x in parsed_json['activemissions'])  # NOQA
                towi_island.activemissions = active_missions
            else:                
                num_order = towi_island.order_missions                
                ses = order(num_order)
                towi_island.order_missions = ses.order
                towi_island.activemissions = ses.games
                towi_island.session_date = timezone.now().date()
            if towi_island.date is None or towi_island.date.date() != timezone.now().date():  # NOQA
                towi_island.date = timezone.now()
                towi_island.activeday += 1
            towi_island.save()
            if children.suscription.active or children.suscription.trial is True:  # NOQA
                response = {'active': True}
            else:
                response = {'active': False}
            return Response(response, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(USER_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)  # NOQA
    else:
        return Response(ERROR_MISSING_JSON, status=status.HTTP_400_BAD_REQUEST)


def order(num_order):
    if num_order == 8 or num_order is None or num_order == 9:
        session = Session.objects.get(order=1)
    else:
        session = Session.objects.get(order=num_order+1)
    return session


@swagger_auto_schema(
    method='POST',
    operation_description="Endpoint that returns if the user have an active childs.",  # NOQA
    operation_summary='api/active_account',
    manual_parameters=[email_param],
    responses={
        200: ActiveAccountSerializer(),
        404: 'USER_NOT_FOUND',
        400: 'ERROR_MISSING_EMAIL_PASSWORD'
        }
)
@api_view(['POST'])
def active_account(request):
    parent_email = request.POST.get('parent_email', None)
    if parent_email is not None:
        try:
            user = User.objects.get(email=parent_email)
            if user.suscriptions.filter(Q(finished_date__gte=timezone.now()) | Q(trial=True)).exists():  # NOQA
                return Response(
                    {
                        'active': True,
                        'suscriptionsAvailables': user.suscriptions.availables().count()  # NOQA
                    }
                )
            else:
                return Response(
                    {
                        'active': False,
                        'suscriptionsAvailables': user.suscriptions.availables().count()  # NOQA
                    }
                )
        except User.DoesNotExist:
            return Response(USER_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(ERROR_MISSING_EMAIL_PASSWORD, status=status.HTTP_400_BAD_REQUEST)  # NOQA


@swagger_auto_schema(method='post', auto_schema=None)
@api_view(['POST'])
def start_trial(request):
    device = request.POST.get('md5_device')
    trial_started_on = request.POST.get('trial_started_on')
    valid_md5 = re.findall(r"([a-fA-F\d]{32})", device)
    if device is not None and valid_md5:
        devices = FreeTrial.objects.filter(md5_device=device)
        if devices.exists():
            return Response({'code': '405', 'trial_id': '{}'.format(devices.first().trial_id)})  # NOQA
        else:
            instance = FreeTrial.objects.create(
                md5_device=device,
            )
            return Response({'code': '200', 'trial_id': '{}'.format(instance.trial_id)})  # NOQA
    else:
        if device is None:
            return Response(ERROR_MISSING_MD5_DEVICE, status=status.HTTP_400_BAD_REQUEST)  # NOQA
        if not valid_md5:
            return Response(ERROR_INVALID_MD5, status=status.HTTP_400_BAD_REQUEST)  # NOQA


@swagger_auto_schema(method='post', auto_schema=None)
@api_view(['POST'])
def consult_trial(request):
    device = request.POST.get('md5_device', None)
    instance = FreeTrial.objects.filter(md5_device=device).first()
    if device is not None:
        if instance:
            delta = instance.trial_id - timezone.now()
            if delta.days > -1:
                return Response({'code': '408'})
            else:
                return Response({'code': '200', 'time_left': '{}'.format(delta)})  # NOQA
        else:
            return Response({'code': '407'})
    else:
        return Response(ERROR_INVALID_MD5, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', auto_schema=None)
@api_view(['POST'])
def register_parent_child(request):
    json_to_parse = request.POST.get('jsonToDb', None)
    parsed_json = json.loads(json_to_parse)
    if parsed_json is not None:
        try:
            validate_email(parsed_json['parent_email'])
        except ValidationError as e:
            return Response(ERROR_INVALID_EMAIL, status=status.HTTP_400_BAD_REQUEST)  # NOQA
        try:
            user = User.objects.get(email=parsed_json['parent_email'])
            return Response({'code': '111'})
        except User.DoesNotExist:
            try:
                user = User.objects.create_user(
                    email=parsed_json['parent_email'],
                    password=parsed_json['parent_password'],
                )
                children = user.create_children(
                    first_name=parsed_json['child_name'],
                    dob=str_to_date(parsed_json['child_dob'])
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
                return Response({
                    'code': '200',
                    'key': user.key,
                    'child_id': str(children.id)
                    })
            except Exception as e:
                if user:
                    user.delete()
                return Response(status=status.HTTP_500_SERVER_ERROR)
    else:
        return Response(ERROR_MISSING_JSON, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', auto_schema=None)
@api_view(['POST'])
def register_child(request):
    json_to_parse = request.POST.get('jsonToDb', None)
    parsed_json = json.loads(json_to_parse)
    if parsed_json is not None:
        try:
            user = User.objects.get(pk=parsed_json['parent_id'])
        except User.DoesNotExist as e:
            return Response(USER_NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)  # NOQA
        try:
            if user.suscriptions.availables():
                children = user.create_children(
                    first_name=parsed_json['child_name'],
                    dob=str_to_date(parsed_json['child_dob'])
                )
                child_suscription = user.suscriptions.availables().first()
                child_suscription.add_children(children)
                ChildrenTowiIsland.create_towi_island(user, children)
                return Response(
                    {
                        'code': '200',
                        'key': user.key,
                        'child_id': children.id,
                        'suscriptionsAvailables': user.suscriptions.availables().count()  # NOQA
                    }
                )
            else:
                data = {
                    'status': 'ERROR',
                    'message': 'The user dont have suscriptions availables'
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if children:
                children.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(ERROR_MISSING_JSON, status=status.HTTP_400_BAD_REQUEST)
