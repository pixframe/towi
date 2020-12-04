# STDLIB IMPORTS
import string
import random

# DJANGO CORE IMPORTS
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.utils import timezone
from django.db.models import Sum
from django.db.models import Count

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


def total_sessions(headers):
    globals = {}
    total_sessions_am = headers.filter(arbolMusicalv2__header__id__isnull=False).count()
    total_sessions_arm = headers.filter(arenaMagicav2__header__id__isnull=False).count()
    total_sessions_dqlb = headers.filter(bolitav2__header__id__isnull=False).count()
    total_sessions_te = headers.filter(tesorov2__header__id__isnull=False).count()
    total_sessions_rio = headers.filter(riov2__header__id__isnull=False).count()
    total_sessions_jds = headers.filter(sombrasv2__header__id__isnull=False).count()
    # total_sessions_he = headers.filter(heladosv2__header__id__isnull=False).count()
    globals.update(
        {
            'total_sessions_am': total_sessions_am,
            'total_sessions_arm': total_sessions_arm,
            'total_sessions_dqlb': total_sessions_dqlb,
      #      'total_sessions_he': total_sessions_he,
            'total_sessions_jds': total_sessions_jds,
            'total_sessions_rio': total_sessions_rio,
            'total_sessions_te': total_sessions_te
        }
    )
    return globals


def total_time_sessions(headers):
    global_time = {}
    total_time_am = headers.filter(arbolMusicalv2__header__id__isnull=False).aggregate(total=Sum('gametime'))
    total_time_arm = headers.filter(arenaMagicav2__header__id__isnull=False).aggregate(total=Sum('gametime'))
    total_time_dqlb = headers.filter(bolitav2__header__id__isnull=False).aggregate(total=Sum('gametime'))
    total_time_te = headers.filter(tesorov2__header__id__isnull=False).aggregate(total=Sum('gametime'))
    total_time_rio = headers.filter(riov2__header__id__isnull=False).aggregate(total=Sum('gametime'))
    total_time_jds = headers.filter(sombrasv2__header__id__isnull=False).aggregate(total=Sum('gametime'))
    # total_time_he = headers.filter(heladosv2__header__id__isnull=False).aggregate(total=Sum('gametime'))
    global_time.update(
        {
            'total_time_am': total_time_am,
            'total_time_arm': total_time_arm,
            'total_time_dqlb': total_time_dqlb,
            # 'total_time_he': total_time_he,
            'total_time_jds': total_time_jds,
            'total_time_rio': total_time_rio,
            'total_time_te': total_time_te
        }
    )
    return global_time


def last_date_session(headers):
    last_date = {}
    last_date_am = headers.filter(arbolMusicalv2__header__id__isnull=False).last()
    last_date_arm = headers.filter(arenaMagicav2__header__id__isnull=False).last()
    last_date_dqlb = headers.filter(bolitav2__header__id__isnull=False).last()
    last_date_te = headers.filter(tesorov2__header__id__isnull=False).last()
    last_date_rio = headers.filter(riov2__header__id__isnull=False).last()
    last_date_jds = headers.filter(sombrasv2__header__id__isnull=False).last()
    # last_date_he = headers.filter(heladosv2__header__id__isnull=False).last()
    last_date.update(
        {
            'last_date_am': last_date_am,
            'last_date_arm': last_date_arm,
            'last_date_dqlb': last_date_dqlb,
            # 'last_date_he': last_date_he,
            'last_date_jds': last_date_jds,
            'last_date_rio': last_date_rio,
            'last_date_te': last_date_te
        }
    )
    return last_date


def first_session(headers):
    first_sessions = {}
    firts_session_am = headers.filter(arbolMusicalv2__header__id__isnull=False).first()
    firts_session_arm = headers.filter(arenaMagicav2__header__id__isnull=False).first()
    firts_session_dqlb = headers.filter(bolitav2__header__id__isnull=False).first()
    firts_session_te = headers.filter(tesorov2__header__id__isnull=False).first()
    firts_session_rio = headers.filter(riov2__header__id__isnull=False).first()
    firts_session_jds = headers.filter(sombrasv2__header__id__isnull=False).first()
    # firts_session_he = headers.filter(heladosv2__header__id__isnull=False).first()
    first_sessions.update(
        {
            'firts_session_am': firts_session_am,
            'firts_session_arm': firts_session_arm,
            'firts_session_dqlb': firts_session_dqlb,
            'firts_session_te': firts_session_te,
            'firts_session_rio': firts_session_rio,
            'firts_session_jds': firts_session_jds,
            # 'firts_session_he': firts_session_he
        }
    )
    return first_sessions


def get_porcentage_correct(headers):
    total_correct_porcentage = {}
    #ArbolMusical
    total_porcentage_am = headers.filter(arbolMusicalv2__header__id__isnull=False).count()
    if total_porcentage_am == 0:
        sum_correct_porcentage = {'total': 0}
        total_correct_am = 0
    else:
        sum_correct_porcentage = headers.filter(arbolMusicalv2__header__id__isnull=False).aggregate(total=Sum('arbolMusicalv2__session_correct_percentage'))
        total_correct_am = sum_correct_porcentage.get('total')
    #ArenaMagica
    total_porcentage_arm = headers.filter(arenaMagicav2__header__id__isnull=False).count()
    if total_porcentage_arm == 0:
        sum_correct_porcentage = {'total': 0}
        total_correct_arm = 0
    else:
        sum_correct_porcentage = headers.filter(arenaMagicav2__header__id__isnull=False).aggregate(total=Sum('arenaMagicav2__session_accuracy_percentage'))
        total_correct_arm = sum_correct_porcentage.get('total') / total_porcentage_arm

    #DondeQuedoLaBolita
    total_porcentage_dqlb = headers.filter(bolitav2__header__id__isnull=False).count()
    if total_porcentage_dqlb == 0:
        sum_correct_porcentage = {'total': 0}
        total_correct_dqlb = 0
    else:
        sum_correct_porcentage = headers.filter(bolitav2__header__id__isnull=False).aggregate(total=Sum('bolitav2__session_correct_percentage'))
        total_correct_dqlb = sum_correct_porcentage.get('total') / total_porcentage_dqlb

    #Tesoro
    total_porcentage_te = headers.filter(tesorov2__header__id__isnull=False).count()
    if total_porcentage_te == 0:
        sum_correct_porcentage = {'total':0}
        total_correct_te = 0
    else:
        sum_correct_porcentage = headers.filter(tesorov2__header__id__isnull=False).aggregate(total=Sum('tesorov2__session_correct_total'))
        total_correct_te = sum_correct_porcentage.get('total') / total_porcentage_te

    #Rio
    total_porcentage_rio = headers.filter(riov2__header__id__isnull=False).count()
    if total_porcentage_rio == 0:
        sum_correct_porcentage = {'total': 0}
        total_correct_rio = 0
    else:
        sum_correct_porcentage = headers.filter(riov2__header__id__isnull=False).aggregate(total=Sum('riov2__session_correct_total'))
        total_correct_rio = sum_correct_porcentage.get('total') / total_porcentage_rio

    #Sombras
    total_porcentage_jds = headers.filter(sombrasv2__header__id__isnull=False).count()
    sum_correct_porcentage = headers.filter(sombrasv2__header__id__isnull=False).aggregate(total=Sum('sombrasv2__session_correct_percentage'))
    if sum_correct_porcentage.get('total') is None:
        total_correct_jds = 0
    else:
        total_correct_jds = sum_correct_porcentage.get('total') / total_porcentage_jds

    #Helados
    # total_porcentage_he = headers.filter(heladosv2__header__id__isnull=False).count() * 100
    # if total_porcentage_he == 0:
    #     sum_correct_porcentage = {'total': 0}
    #     total_correct_he = 0
    # else:
    #     sum_correct_porcentage = headers.filter(heladosv2__header__id__isnull=False).aggregate(total=Sum('heladosv2__session_correct_percentage'))
    #     total_correct_he = sum_correct_porcentage.get('total')* 100 / total_porcentage_he

    total_correct_porcentage.update(
        {
            'total_correct_am': total_correct_am,
            'total_correct_arm': total_correct_arm,
            'total_correct_dqlb': total_correct_dqlb,
            'total_correct_te': total_correct_te,
            'total_correct_rio': total_correct_rio,
            'total_correct_jds': total_correct_jds,
            # 'total_correct_he': total_correct_he
        }
    )
    return total_correct_porcentage


def get_porcentage_errors(headers):
    total_errors_porcentage = {}
    #ArbolMusical
    total_porcentage_am = headers.filter(arbolMusicalv2__header__id__isnull=False).count()
    if total_porcentage_am == 0:
        sum_errors_porcentage = {'total': 0}
        total_errors_am = 0
    else:
        sum_errors_porcentage = headers.filter(arbolMusicalv2__header__id__isnull=False).aggregate(total=Sum('arbolMusicalv2__session_errors_percentage'))
        total_errors_am = sum_errors_porcentage.get('total') / total_porcentage_am
    #ArenaMagica
    total_porcentage_arm = headers.filter(arenaMagicav2__header__id__isnull=False).count()
    if total_porcentage_arm == 0:
        sum_errors_porcentage = {'total': 0}
        total_errors_arm = 0
    else:
        sum_errors_porcentage = headers.filter(arenaMagicav2__header__id__isnull=False).aggregate(total=Sum('arenaMagicav2__session_overdraw_percentage'))
        total_errors_arm = sum_errors_porcentage.get('total') / total_porcentage_arm

    #DondeQuedoLaBolita
    total_porcentage_dqlb = headers.filter(bolitav2__header__id__isnull=False).count()
    if total_porcentage_dqlb == 0:
        sum_errors_porcentage = {'total': 0}
        total_errors_dqlb = 0
    else:
        sum_errors_porcentage = headers.filter(bolitav2__header__id__isnull=False).aggregate(total=Sum('bolitav2__session_errors_percentage'))
        total_errors_dqlb = sum_errors_porcentage.get('total') / total_porcentage_dqlb

    #Tesoro
    total_porcentage_te = headers.filter(tesorov2__header__id__isnull=False).count()
    if total_porcentage_te == 0:
        sum_errors_porcentage = {'total':0}
        total_errors_te = 0
    else:
        sum_errors_porcentage = headers.filter(tesorov2__header__id__isnull=False).aggregate(total=Sum('tesorov2__session_errors_total'))
        total_errors_te = sum_errors_porcentage.get('total') / total_porcentage_te

    #Rio
    total_porcentage_rio = headers.filter(riov2__header__id__isnull=False).count()
    if total_porcentage_rio == 0:
        sum_errors_porcentage = {'total': 0}
        total_errors_rio = 0
    else:
        sum_errors_porcentage = headers.filter(riov2__header__id__isnull=False).aggregate(total=Sum('riov2__session_errors_total'))
        total_errors_rio = sum_errors_porcentage.get('total') / total_porcentage_rio

    #Sombras
    total_porcentage_jds = headers.filter(sombrasv2__header__id__isnull=False).count()
    sum_errors_porcentage = headers.filter(sombrasv2__header__id__isnull=False).aggregate(total=Sum('sombrasv2__session_errors_percentage'))
    if sum_errors_porcentage.get('total') is None:
        total_errors_jds = 0
    else:
        total_errors_jds = sum_errors_porcentage.get('total') / total_porcentage_jds

    #Helados
    # total_porcentage_he = headers.filter(heladosv2__header__id__isnull=False).count() * 100
    # if total_porcentage_he == 0:
    #     sum_errors_porcentage = {'total': 0}
    #     total_errors_he = 0
    # else:
    #     sum_errors_porcentage = headers.filter(heladosv2__header__id__isnull=False).aggregate(total=Sum('heladosv2__session_errors_percentage'))
    #     total_errors_he = sum_errors_porcentage.get('total')* 100 / total_porcentage_he

    total_errors_porcentage.update(
        {
            'total_errors_am': total_errors_am,
            'total_errors_arm': total_errors_arm,
            'total_errors_dqlb': total_errors_dqlb,
            'total_errors_te': total_errors_te,
            'total_errors_rio': total_errors_rio,
            'total_errors_jds': total_errors_jds,
            # 'total_errors_he': total_errors_he
        }
    )
    return total_errors_porcentage