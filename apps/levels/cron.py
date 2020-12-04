from django.utils import timezone
from levels.models.v1_models import TowiIndex, Session, ChildrenTowiIsland


def restart_active_missions():
    """
    Task to update all empty games in childrentowiislands
    daily
    :return: None
    """
    print("++++++ iniciado tarea de restart_active_missions ... version 3 +++++")
    session = Session.objects.exclude(order=0).order_by('?').first()
    ChildrenTowiIsland.objects.all().update(
        activemissions=str(session.games),
        date=timezone.now()
    )
    '''ChildrenTowiIsland.objects.filter(
        Q(activemissions__isnull=True) |
        Q(activemissions='')
    ).update(
        activemissions=str(session.games),
        date=timezone.now()
    )
    '''
    print("------ finalizando tarea de restart_active_missions ...  version 3---- ")
    return