import pytz
from datetime import datetime
from django.utils import timezone

def str_to_date(str):
    date = datetime.strptime(str, "%Y-%m-%d").date()
    return date


def str_to_datetime(str):
    try:
        date = datetime.strptime(str, "%Y-%m-%dT%H:%M:%S")
        date = timezone.make_aware(date)
        return date
    except Exception as e:
        return False


def str_to_bool(string):
    if string in ['True', 'true', 1]:
        return True
    elif string in ['False', 'false', 0]:
        return False
    else:
        return False


def grade_string(string):
    if string.startswith('K') or string.startswith('k'):
        return 'Kinder'
    elif string.startswith('P') or string.startswith('p'):
        return 'Preprimaria'
    elif string.startswith('1'):
        return '1 primaria'
    elif string.startswith('2'):
        return '2 primaria'
    elif string.startswith('3'):
        return '3 primaria'
    elif string.startswith('4'):
        return '4 primaria'
    elif string.startswith('5'):
        return '5 primaria'
    elif string.startswith('6'):
        return '6 primaria'
    else:
        return 'Kinder'
