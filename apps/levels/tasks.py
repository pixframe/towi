from celery.task import periodic_task
from celery import shared_task
from django.db.models import Q, Sum
from celery.schedules import crontab
from .models import ChildrenTowiIsland, Session
from django.utils import timezone
from accounts.models import User, Children
from levels.models.v1_models import TowiIndex


@periodic_task(run_every=crontab(hour=10, minute=00))
def assign_games():
    """
    Task to update all empty games in childrentowiislands
    daily
    :return: None
    """
    print("iniciado tarea de assing_games ...")
    session = Session.objects.exclude(order=0).order_by('?').first()
    ChildrenTowiIsland.objects.filter(
        Q(activemissions__isnull=True) |
        Q(activemissions='')
    ).update(
        activemissions=str(session.games),
        date=timezone.now()
    )
    print("finalizando tarea de assing_games ...")
    return

@shared_task
def towi_index(userKey, cid, gameKey, date):
    """
    Task to update index game
    """
    if userKey is not None and cid is not None and gameKey is not None and date is not None:  # NOQA
        try:
            user = User.objects.get(key=userKey)
        except User.ObjectDoesNotExist:
            return 
        towi_index_qs = user.towiIndex.filter(
            cid=cid,
            gamekey=gameKey
        ).order_by('-date')[:2]
        current_index = 0
        empty_index = 0
        exists = False
        if towi_index_qs.exists():
            instance = towi_index_qs.first()
            current_index = instance.index
            if instance.date.strftime('%Y-%m-%d') == date:
                return
        else:
            empty_index = True
        update_index = False
        index_update = 0
        if gameKey == 'ArenaMagica':
            headers = user.headers.filter(
                cid=cid,
                date__startswith=date,
                gamekey='ArenaMagica'
            )
            headers_sum = headers.aggregate(
                Sum('playedlevels'),
                Sum('repeatedlevels'),
                Sum('passedlevels')
            )
            if headers_sum['playedlevels__sum'] not in [0, None]:
                levels = headers.first().arenaMagicav2.all()
                accuracy = 0
                passed = 0
                if levels:
                    for l in levels:
                        accuracy += l.session_accuracy_percentage
                        passed += l.session_overdraw_percentage
                    index_p1 = ((passed/levels.count())*100)*0.5
                    index_p2 = ((accuracy/levels.count())*100)*0.5
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((passed/levels.count())*6-3)*0.5
                    index_p2 = (((accuracy/levels.count())/100*6)-3)*0.5
                    index_update = index_p1 + index_p2

                    update_index = True
                else:
                    update_index = False
                    return 
            else:
                update_index = False
                return 
        elif gameKey == 'ArbolMusical':
            headers = user.headers.filter(cid=cid, date__startswith=date, gamekey='ArbolMusical')
            headers_sum = headers.aggregate(Sum('playedlevels'), Sum('repeatedlevels'), Sum('passedlevels'))
            if headers_sum['playedlevels__sum'] not in [0, None]:
                header = headers.first()
                levels = header.arbolMusicalv2.all()
                correct = 0
                errors = 0
                passed = 0
                if levels:
                    for l in levels:
                        correct += l.total_correct
                        errors += l.total_errors
                    index_p1 = ((header.passedlevels/header.playedlevels)*100)*0.5
                    index_p2 = ((correct/(correct+errors))*100)*0.5
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((header.passedlevels/header.playedlevels)*6-3)*0.5
                    index_p2 = (((correct/(correct+errors))*6)-3)*0.5
                    index_update = index_p1 + index_p2
                    update_index = True
                else:
                    update_index = False
                    return 
            else:
                update_index = False
                return 
        elif gameKey == 'DondeQuedoLaBolita':
            headers = user.headers.filter(cid=cid, date__startswith=date, gamekey='DondeQuedoLaBolita')
            headers_sum = headers.aggregate(Sum('playedlevels'), Sum('repeatedlevels'), Sum('passedlevels'))
            if headers_sum['playedlevels__sum'] not in [0, None]:
                header = headers.first()
                levels = header.bolitav2.all()
                correct = 0
                errors = 0
                passed = 0
                if levels:
                    for l in levels:
                        correct += l.correct_monkeys
                        errors += l.errors_monkeys
                    index_p1 = ((header.passedlevels/header.playedlevels)*100)*0.5
                    index_p2 = ((correct/(correct+errors))*100)*0.5
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((header.passedlevels/header.playedlevels)*6-3)*0.5
                    index_p2 = (((correct/(correct+errors))*6)-3)*0.5
                    index_update = index_p1 + index_p2
                    update_index = True
                else:
                    update_index = False
                    return 
            else:
                update_index = False
                return 
        elif gameKey == 'Rio':
            headers = user.headers.filter(cid=cid, date__startswith=date, gamekey='Rio')
            headers_sum = headers.aggregate(Sum('playedlevels'), Sum('repeatedlevels'), Sum('passedlevels'))
            if headers_sum['playedlevels__sum'] not in [0, None]:
                header = headers.first()
                levels = header.riov2.all()
                correct = 0
                errors = 0
                passed = 0
                if levels:
                    for l in levels:
                        correct += l.target_correct
                        errors += l.target_errors
                    index_p1 = ((header.passedlevels/header.playedlevels)*100)*0.5
                    index_p2 = ((correct/(correct+errors))*100)*0.5   # ATENCION AQUI ORIGINAL NO MULTIPLICABA PRIMERO POR 100
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((header.passedlevels/header.playedlevels)*6-3)*0.5
                    index_p2 = (((correct/(correct+errors))*6)-3)*0.5   # ATENCION AQUI ORIGINAL NO MULTIPLICABA PRIMERO POR 100
                    index_update = index_p1 + index_p2
                    update_index = True
                else:
                    update_index = False
                    return 
            else:
                update_index = False
                return 
        elif gameKey == 'Tesoro':
            headers = user.headers.filter(cid=cid, date__startswith=date, gamekey='Tesoro')
            headers_sum = headers.aggregate(Sum('playedlevels'), Sum('repeatedlevels'), Sum('passedlevels'))
            if headers_sum['playedlevels__sum'] not in [0, None]:
                header = headers.first()
                levels = header.tesorov2.all()
                correct = 0
                errors = 0
                passed = 0
                if levels:
                    for l in levels:
                        correct += l.session_correct_total
                        errors += l.session_errors_total
                    index_p1 = ((header.passedlevels/header.playedlevels)*100)*0.5
                    index_p2 = ((correct/(correct+errors))*100)*0.5
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((header.passedlevels/header.playedlevels)*6-3)*0.5
                    index_p2 = (((correct/(correct+errors))*6)-3)*0.5
                    index_update = index_p1 + index_p2
                    update_index = True
                else:
                    update_index = False
                    return 
            else:
                update_index = False
                return 
        elif gameKey == 'JuegoDeSombras':
            headers = user.headers.filter(cid=cid, date__startswith=date, gamekey='JuegoDeSombras')
            headers_sum = headers.aggregate(Sum('playedlevels'), Sum('repeatedlevels'), Sum('passedlevels'))
            if headers_sum['playedlevels__sum'] not in [0, None]:
                header = headers.first()
                levels = header.sombrasv2.all()
                correct = 0
                errors = 0
                passed = 0
                if levels:
                    for l in levels:
                        correct += l.session_correct_percentage
                        errors += l.session_errors_percentage
                    index_p1 = ((header.passedlevels/header.playedlevels)*100)*0.5
                    index_p2 = ((correct/(correct+errors))*100)*0.5
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((header.passedlevels/header.playedlevels)*6-3)*0.5
                    index_p2 = (((correct/(correct+errors))*6)-3)*0.5
                    index_update = index_p1 + index_p2
                    update_index = True
                else:
                    update_index = False
                    return 
            else:
                update_index = False
                return 
        if update_index:
            if exists:
                return 
            else:
                if empty_index:
                    index_update = index_update_new
                towiIndex = TowiIndex.objects.create(
                    parent=user,
                    cid=Children.objects.get(pk=cid),
                    date=date,
                    gamekey=gameKey,
                    index=current_index + index_update,
                    serverdate=timezone.now()
                )
                return 
    else:
        return 