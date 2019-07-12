# Django Core Libraries
from django.db.models import Sum

# Third-party libraries
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Own´s Libraries
from towi_framework.viewsets import CreateLevelView, CreateCustomView
from .serializers import (
    AssesmentSerializer,
    JsonDataSerializer,
    HeaderCreateSerializer,
    ArbolMusicalSerializer,
    ArenaMagicaSerializer,
    DondeQuedoLaBolitaSerializer,
    RioSerializer,
    TesoroSerializer,
    JuegoDeSombrasSerializer,
)
from ...models import (
    Prueba,
    ArbolMusicalV2,
    ArenaMagicaV2,
    RecoleccionTesoroV2,
    DondeQuedoLaBolitaV2,
    RioV2,
    SombrasV2,
)
from accounts.models import User
from reusable.helpers import str_to_date


class AssesmentCreateView(CreateCustomView):
    '''
    A view to retrieve a user instance
    created by @christianbos
    '''
    serializer_class = AssesmentSerializer
    queryset = Prueba.objects.get_queryset()
    json_serializer_class = JsonDataSerializer
    header_serializer_class = HeaderCreateSerializer


class LevelsView(CreateLevelView):
    '''
        A view to retrieve a user instance
        created by @christianbos
    '''
    queryset = Prueba.objects.get_queryset()
    ArbolMusical_serializer_class = ArbolMusicalSerializer
    Rio_serializer_class = RioSerializer
    ArenaMagica_serializer_class = ArenaMagicaSerializer
    DondeQuedoLaBolita_serializer_class = DondeQuedoLaBolitaSerializer
    Tesoro_serializer_class = TesoroSerializer
    JuegoDeSombras_serializer_class = JuegoDeSombrasSerializer
    json_serializer_class = JsonDataSerializer
    header_serializer_class = HeaderCreateSerializer


class ChildrenLevelsView(APIView):
    def post(self, request):
        userKey = request.POST.get('userKey', None)
        cid = request.POST.get('cid', None)
        date = request.POST.get('date', None)
        date = str_to_date(date)
        if userKey is not None and cid is not None and date is not None:
            user = User.objects.get(key=userKey)
            child = user.childrens.get(id=cid)
            headers = user.headers.filter(cid=child)
            if headers:
                arbolMusical = ArbolMusicalV2.objects.filter(header__in=headers, header__gamekey='ArbolMusical').last()
                rio = RioV2.objects.filter(header__in=headers, header__gamekey='Rio').last()
                arenaMagica = ArenaMagicaV2.objects.filter(header__in=headers, header__gamekey='ArenaMagica').last()
                bolita = DondeQuedoLaBolitaV2.objects.filter(header__in=headers, header__gamekey='DondeQuedoLaBolita').last()
                tesoro = RecoleccionTesoroV2.objects.filter(header__in=headers, header__gamekey='Tesoro').last()
                sombras = SombrasV2.objects.filter(header__in=headers, header__gamekey='JuegoDeSombras').last()
                headers = headers.filter(date__startswith=date)
                data = {
                    "code": "200",
                    "arbolMusicalLevel": arbolMusical.current_difficulty if arbolMusical else 0,
                    "arbolMusicalSublevel": arbolMusical.current_level if arbolMusical else 0,
                    "rioLevel": rio.current_difficulty if rio else 0,
                    "rioSublevel": rio.current_level if rio else 0,
                    "arenaMagicaLevel": arenaMagica.current_level if arenaMagica else 0,
                    "arenaMagicaSublevel": arenaMagica.current_level_motor if arenaMagica else 0,
                    "arenaMagicaSublevel2": arenaMagica.current_level_overlapping if arenaMagica else 0,
                    "arenaMagicaSublevel3": arenaMagica.current_level_clousre if arenaMagica else 0,
                    "monkeyLevel": bolita.current_difficulty if bolita else 0,
                    "monkeySublevel": bolita.current_level if bolita else 0,
                    "sombrasLevel": sombras.current_difficulty if sombras else 0,
                    "sombrasSublevel": sombras.current_level if sombras else 0,
                    "tesoroLevel": tesoro.current_difficulty if tesoro else 0,
                    "tesoroSublevel": tesoro.current_level if tesoro else 0,
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