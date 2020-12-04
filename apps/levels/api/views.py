# STDLIB IMPORTS
import json
import pytz
from datetime import datetime

# DJANGO CORE IMPORTS
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.utils import timezone

# THIRD PARTY IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# TOWI IMPORTS
from accounts.models import User, Children
from ..models import Header, Prueba, ArbolMusical, \
    ArenaMagica, RecoleccionTesoro, DondeQuedoLaBolita, \
    TowiIndex, Rio, Sombras
from reusable.responses import *
from reusable.helpers import str_to_date, str_to_datetime
from reusable.docs import *
from .serializers import *


@swagger_auto_schema(
    method='POST',
    operation_description="Endpoint to create the TOWI Index.",
    operation_summary='api/towi_index',
    manual_parameters=[userkey_param, gamekey_param, date_param, cid_param],
    responses={
        200: CodeSerializer(),
        400: 'ERROR_MISSING_PARAMETERS'
        }
)
@api_view(['POST'])
def towi_index(request):
    userKey = request.POST.get('userKey', None)
    cid = request.POST.get('cid', None)
    gameKey = request.POST.get('gameKey', None)
    date = request.POST.get('date', None)
    if userKey is not None and cid is not None and gameKey is not None and date is not None:  # NOQA
        try:
            user = User.objects.get(key=userKey)
        except User.ObjectDoesNotExist:
            return Response(USER_NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)
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
                return Response({"code": "200"})
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
                levels = headers.first().arenaMagica.all()
                accuracy = 0
                passed = 0
                if levels:
                    for l in levels:
                        accuracy += l.accuracy
                        passed += l.passed
                    index_p1 = ((passed/levels.count())*100)*0.5
                    index_p2 = ((accuracy/levels.count())*100)*0.5
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((passed/levels.count())*6-3)*0.5
                    index_p2 = (((accuracy/levels.count())/100*6)-3)*0.5
                    index_update = index_p1 + index_p2

                    update_index = True
                else:
                    update_index = False
                    return Response({"code": "400"})
            else:
                update_index = False
                return Response({"code": "400"})
        elif gameKey == 'ArbolMusical':
            headers = user.headers.filter(cid=cid, date__startswith=date, gamekey='ArbolMusical')
            headers_sum = headers.aggregate(Sum('playedlevels'), Sum('repeatedlevels'), Sum('passedlevels'))
            if headers_sum['playedlevels__sum'] not in [0, None]:
                header = headers.first()
                levels = header.arbolMusical.all()
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
                    return Response({"code": "400"})
            else:
                update_index = False
                return Response({"code": "400"})
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
                    return Response({"code": "400"})
            else:
                update_index = False
                return Response({"code": "400"})
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
                        correct += l.session_errors_total
                        errors += l.session_errors_total
                    index_p1 = ((header.passedlevels/header.playedlevels)*100)*0.5
                    index_p2 = ((correct/(correct+errors))*100)*0.5   # ATENCION AQUI ORIGINAL NO MULTIPLICABA PRIMERO POR 100
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((header.passedlevels/header.playedlevels)*6-3)*0.5
                    index_p2 = (((correct/(correct+errors))*6)-3)*0.5   # ATENCION AQUI ORIGINAL NO MULTIPLICABA PRIMERO POR 100
                    index_update = index_p1 + index_p2
                    update_index = True
                else:
                    update_index = False
                    return Response({"code": "400"})
            else:
                update_index = False
                return Response({"code": "400"})
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
                    return Response({"code": "400"})
            else:
                update_index = False
                return Response({"code": "400"})
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
                        correct += l.correct
                        errors += l.errors
                    index_p1 = ((header.passedlevels/header.playedlevels)*100)*0.5
                    index_p2 = ((correct/(correct+errors))*100)*0.5
                    index_update_new = index_p1 + index_p2

                    index_p1 = ((header.passedlevels/header.playedlevels)*6-3)*0.5
                    index_p2 = (((correct/(correct+errors))*6)-3)*0.5
                    index_update = index_p1 + index_p2
                    update_index = True
                else:
                    update_index = False
                    return Response({"code": "400"})
            else:
                update_index = False
                return Response({"code": "400"})
        if update_index:
            if exists:
                return Response({"code": "200"})
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
                return Response({"code": "200"})
    else:
        return Response(ERROR_MISSING_PARAMETERS, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='POST',
    operation_description="Endpoint to save the test data.",
    operation_summary='api/pruebas',
    manual_parameters=[json_param],
    responses={
        200: CodeSerializer(),
        400: 'ERROR_MISSING_JSON'
        }
)
@api_view(['POST'])
def pruebas(request):
    string_to_parse = request.POST.get('jsonToDb', None)
    if string_to_parse is not None:
        header, levels = string_to_json(string_to_parse)
        if header is False:
            return Response(ERROR_PARSING_JSON, status=status.HTTP_400_BAD_REQUEST)  # NOQA
        header_instance = create_header_instance(header)
        if header_instance is False:
            return Response(USER_NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)
        try:
            instance_pruebas = Prueba.objects.create(
                header=header_instance,
                **levels
            )
        except Exception as e:
            return Response({"code": 404, "error": "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'code': "200"})
    return Response(ERROR_MISSING_JSON, status=status.HTTP_400_BAD_REQUEST)  # NOQA


@swagger_auto_schema(
    method='POST',
    operation_description="Endpoint to save the data of the levels.",
    operation_summary='api/levels',
    manual_parameters=[json_param],
    responses={
        200: CodeSerializer(),
        400: 'ERROR_MISSING_JSON'
        }
)
@api_view(['POST'])
def levels(request):
    string_to_parse = request.POST.get('jsonToDb', None)
    if string_to_parse is not None:
        header, levels = string_to_json(string_to_parse)
        if header is False:
            return Response(ERROR_PARSING_JSON, status=status.HTTP_400_BAD_REQUEST)  # NOQA
        header_instance = create_header_instance(header)
        if header_instance is False:
            return Response(USER_NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)
        if header_instance.gamekey == 'ArbolMusical':
            for level in levels:
                ArbolMusical.objects.create(
                    header=header_instance,
                    **level
                )
            return Response({'code': "200"})

        elif header_instance.gamekey == 'ArenaMagica':
            for level in levels:
                ArenaMagica.objects.create(
                    header=header_instance,
                    **level
                )
            return Response({'code': "200"})

        elif header_instance.gamekey == 'DondeQuedoLaBolita':
            for level in levels:
                DondeQuedoLaBolita.objects.create(
                    header=header_instance,
                    **level
                )
            return Response({'code': "200"})

        elif header_instance.gamekey == 'Tesoro':
            for level in levels:
                RecoleccionTesoro.objects.create(
                    header=header_instance,
                    **level
                )
            return Response({'code': "200"})

        elif header_instance.gamekey == 'Rio':
            for level in levels:
                Rio.objects.create(
                    header=header_instance,
                    **level
                )
            return Response({'code': "200"})

        elif header_instance.gamekey == 'JuegoDeSombras':
            for level in levels:
                Sombras.objects.create(
                    header=header_instance,
                    **level
                )
            return Response({'code': "200"})

        else:
            return Response({'code': '400', 'status': 'GAMEKEY_NOT_FOUND'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(ERROR_MISSING_JSON, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='POST',
    operation_description="Endpoint to get the last level, sub-level of the games and the levels played of a day.",
    operation_summary='api/levels',
    manual_parameters=[userkey_param, cid_param, date_param],
    responses={
        200: ChildrenLevelsSerializer(),
        400: 'ERROR_MISSING_PARAMETERS'
        }
)
@api_view(['POST'])
def get_children_levels(request):
    userKey = request.POST.get('userKey', None)
    cid = request.POST.get('cid', None)
    date = request.POST.get('date', None)
    date = str_to_date(date)
    if userKey is not None and cid is not None and date is not None:
        user = User.objects.get(key=userKey)
        child = user.childrens.get(id=cid)
        headers = user.headers.filter(cid=child)
        if headers:
            arbolMusical = ArbolMusical.objects.filter(header__in=headers, header__gamekey='ArbolMusical').last()
            rio = Rio.objects.filter(header__in=headers, header__gamekey='Rio').last()
            arenaMagica = ArenaMagica.objects.filter(header__in=headers, header__gamekey='ArenaMagica').last()
            bolita = DondeQuedoLaBolita.objects.filter(header__in=headers, header__gamekey='DondeQuedoLaBolita').last()
            tesoro = RecoleccionTesoro.objects.filter(header__in=headers, header__gamekey='Tesoro').last()
            sombras = Sombras.objects.filter(header__in=headers, header__gamekey='JuegoDeSombras').last()
            headers = headers.filter(date__startswith=date)
            data = {
                "code": "200",
                "arbolMusicalLevel": arbolMusical.level if arbolMusical else 0,
                "arbolMusicalSublevel": arbolMusical.sublevel if arbolMusical else 0,
                "rioLevel": rio.level if rio else 0,
                "rioSublevel": rio.sublevel if rio else 0,
                "arenaMagicaLevel": arenaMagica.level if arenaMagica else 0,
                "arenaMagicaSublevel": arenaMagica.sublevel if arenaMagica else 0,
                "arenaMagicaSublevel2": arenaMagica.sublevel2 if arenaMagica else 0,
                "arenaMagicaSublevel3": arenaMagica.sublevel3 if arenaMagica else 0,
                "monkeyLevel": bolita.level if bolita else 0,
                "monkeySublevel": bolita.sublevel if bolita else 0,
                "sombrasLevel": sombras.level if sombras else 0,
                "sombrasSublevel": sombras.sublevel if sombras else 0,
                "tesoroLevel": tesoro.level if tesoro else 0,
                "tesoroSublevel": tesoro.sublevel if tesoro else 0,
                "arbolToday": headers.filter(gamekey='ArbolMusical').aggregate(Sum('playedlevels'))['playedlevels__sum'] or 0,
                "rioToday": headers.filter(gamekey='Rio').aggregate(Sum('playedlevels'))['playedlevels__sum'] or 0,
                "arenaToday": headers.filter(gamekey='ArenaMagica').aggregate(Sum('playedlevels'))['playedlevels__sum'] or 0,
                "monkeyToday": headers.filter(gamekey='DondeQuedoLaBolita').aggregate(Sum('playedlevels'))['playedlevels__sum'] or 0,
                "sombrasToday": headers.filter(gamekey='JuegoDeSombras').aggregate(Sum('playedlevels'))['playedlevels__sum'] or 0,
                "tesoroToday": headers.filter(gamekey='Tesoro').aggregate(Sum('playedlevels'))['playedlevels__sum'] or 0
            }
            return Response(data)

        else:
            data = {
                "code": "200",
                "arbolMusicalLevel": 0,
                "arbolMusicalSublevel": 0,
                "rioLevel": 0,
                "rioSublevel": 0,
                "arenaMagicaLevel": 0,
                "arenaMagicaSublevel": 0,
                "arenaMagicaSublevel2": 0,
                "arenaMagicaSublevel3": 0,
                "monkeyLevel": 0,
                "monkeySublevel": 0,
                "sombrasLevel": 0,
                "sombrasSublevel": 0,
                "tesoroLevel": 0,
                "tesoroSublevel": 0,
                "arbolToday": 0,
                "rioToday": 0,
                "arenaToday": 0,
                "monkeyToday": 0,
                "sombrasToday": 0,
                "tesoroToday": 0
            }
            return Response(data)
    else:
        return Response(ERROR_MISSING_PARAMETERS, status=status.HTTP_400_BAD_REQUEST)


def create_header_instance(header):
    try:
        parent = User.objects.get(id=header['parentid'])
        cid = parent.childrens.get(id=header['cid'])
    except ObjectDoesNotExist:
        return False
    date = str_to_datetime(header['date'])
    if date is False:
        date = timezone.now()
    header_instance = Header.objects.filter(
        date=date,
        parent=parent,
        cid=cid,
        gamekey=header['gameKey']
    ).first()
    if header_instance:
        header_instance.gametime + header['gameTime']
        header_instance.passedlevels + header['passedLevels']
        header_instance.repeatedlevels + header['repeatedLevels']
        header_instance.playedlevels + header['playedLevels']
        header_instance.save()
    else:
        application_number = cid.headers.filter(gamekey=header['gameKey']).count() + 1
        header_instance = Header(
            date=date,
            parent=parent,
            cid=cid,
            gamekey=header['gameKey'],
            gametime=header['gameTime'],
            passedlevels=header['passedLevels'],
            repeatedlevels=header['repeatedLevels'],
            playedlevels=header['playedLevels'],
            device=header['device'],
            version=header['version'],
            application_number=application_number
        )
        header_instance.save()
    return header_instance


def string_to_json(string):
    try:
        json_parsed = json.loads(string)
        header = json_parsed['header']
        levels_upper = json_parsed['levels']
        if isinstance(levels_upper, list):
            levels = []
            for level in levels_upper:
                levels.append({k.lower(): v for k, v in level.items()})
        else:
            levels = {k.lower(): v for k, v in levels_upper.items()}
    except Exception as e:
        print(string)
        return False, False

    return header, levels


@api_view(['GET'])
def connection_reach(request):
    return Response({'connection': 'Reached'})