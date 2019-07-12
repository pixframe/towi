# STDLIB IMPORTS
import string
import random

# DJANGO CORE IMPORTS
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.utils import timezone

# THIRD APPS IMPORTS
from rest_framework_jwt.settings import api_settings


def create_order_id(suscription_id):
    time = timezone.now().strftime("%Y%m%d%H%M%S")
    string = time + '-' + str(suscription_id)
    return string


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


def generate_jwt(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def str2date(datestr="", formato="%d/%m/%Y"):
    try:
        if datestr in [None, '00-00-0000']:
            return None
        date_str = datestr.split(' ')[0]
        return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    except Exception as e:
        return None


def activity_to_english(activity, full=False):
    if activity == 'PruebaEcologica':
        if full is True:
            return 'Towi-Assessment-Full'
        return 'Towi-Assessment'
    elif activity == 'ArbolMusical':
        if full is True:
            return 'Birds-Game-Full'
        return 'Birds-Game'
    elif activity == 'ArenaMagica':
        if full is True:
            return 'Sand-Game-Full'
        return 'Sand-Game'
    elif activity == 'Rio':
        if full is True:
            return 'River-Game-Full'
        return 'River-Game'
    elif activity == 'Tesoro':
        if full is True:
            return 'Quest-Game-Full'
        return 'Quest-Game'
    elif activity == 'JuegoDeSombras':
        if full is True:
            return 'Shadows-Game-Full'
        return 'Shadows-Game'
    elif activity == 'DondeQuedoLaBolita':
        if full is True:
            return 'Monkeys-Game-Full'
        return 'Monkeys-Game'
