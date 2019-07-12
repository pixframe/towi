# Django Core Imports
from .models import ChildrenTowiIsland, Session


def session_changer(cti_id):
    try:
        instance = ChildrenTowiIsland.objects.get(pk=cti_id)
        if instance.cid.active is True:
            session_instance = Session.objects.order_by("?").first()
            instance.activemissions = session_instance.games
            instance.save()
        else:
            instance_towi_island.activemissions = []
    except ChildrenTowiIsland.DoesNotExist:
        pass


#Methods for changue to english
def changue_laterality_to_english(value):
    if value == 'derecho' or value == 'Diestro':
        return 'Right'
    elif value == 'zurdo':
        return 'Left'
    elif value == 'desconocido':
        return 'unknown'
    return value


def changue_genre_to_english(value):
    if value == 'Masculino':
        return 'Male'
    elif value == 'Femenino':
        return 'Female'
    else:
        return 'Other'


def changue_grade_to_english(value):
    if value == 'Kinder':
        return 'Kindergarten'
    elif value == '1 primaria' or value == '1 Primaria':
        return '1 Primary'
    elif value == '2 primaria' or value == '2° Primaria':
        return '2 primary'
    elif value == '3 primaria' or value == '3° Primaria':
        return '3 primary'
    elif value == '4 primaria' or value == '4° Primaria':
        return '4 primary'
    elif value == '5 primaria' or value == '5° Primaria':
        return '5 primary'
    elif value == '6 primaria' or value == '6° Primaria':
        return '6 primary'
    elif value == 'Preprimaria':
        return 'Preprimary'
    return value