import string
import random
from django.core.management.base import BaseCommand, CommandError
from reusable.models import Users, Children, UserType, ValidationIds
from reusable.models import RioLevels as RL
from reusable.models import ArbolmusicalLevels as AL
from reusable.models import ArbolmusicalHeaders as AH
from reusable.models import ArenamagicaHeaders as AMH
from reusable.models import ArenamagicaLevels as AML
from reusable.models import DondequedolabolitaHeaders as DBH
from reusable.models import DondequedolabolitaLevels as DBL
from reusable.models import PruebasHeadersNew as PH
from reusable.models import PruebasLevelsNew as PL
from reusable.models import RecolecciondeltesoroHeaders as RTH
from reusable.models import RecolecciondeltesoroLevels as RTL
from reusable.models import RioHeaders as RH
from reusable.models import ShadowsHeaders as SH
from reusable.models import ShadowsLevels as SL
from reusable.models import Children as Ninos
from reusable.models import UserType as TipoUsuario
from reusable.models import ValidationIds as Vin
from reusable.models import TowiIndex as Ti
from reusable.models import ChildrenTowiIsland as CH
from reusable.helpers import grade_string
from levels.models import *
from suscriptions.models import *
from accounts.models import Children as Child
from accounts.models import User
from accounts.models import UserType as Utype
from dashboard.helpers import str2date
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):
    help = 'Importa la base vieja a la nueva'

    def handle(self, *args, **options):
        import pudb; pudb.set_trace()
        for u in Users.objects.all():  # id 22 elena
            try:
                va_id = Vin.objects.filter(
                    pid=u.id
                ).first()
                user_type_k = TipoUsuario.objects.filter(
                    id=u.user_type
                ).first()
                try:
                    user = User.objects.get(
                        email=u.email
                    )
                except ObjectDoesNotExist as i:
                    user = User.objects.create_user(
                        first_name=u.name,
                        last_name=u.lastname,
                        country=u.country,
                        state=u.state,
                        genre=u.genre,
                        relation=u.relation,
                        verified=u.verified,
                        email=u.email,
                        dob=u.dob,
                        date_joined=u.register_date,
                        is_active=True,
                        is_staff=False,
                        password='1',
                        user_type=user_type_k.description if user_type_k else 'familiar',
                    )
                kids = Ninos.objects.filter(parentid=u.id)
                for c in kids:
                    if user is not None:
                        try:
                            child, c_created = Child.objects.get_or_create(
                                user=user,
                                first_name=c.name,
                                last_name=c.lastname,
                                dob=str2date(c.dob),
                                grade=grade_string(c.grade),
                                genre=c.genre,
                                email=c.email,
                                register_date=c.register_date,
                                active=c.active,
                                trial_active=c.trial_active,
                            )
                            if hasattr(child, 'suscription') is False:
                                Suscription.create_new(user, 'unsuscribe', ids=[child.id])
                        except Exception as e:
                            print('child id {} - {}'.format(c.id, e))
                    for e in AH.objects.filter(cid=c.id, parentid=u.id):
                        levels = AL.objects.filter(headerid=e.id)
                        if levels:
                            header, h_created = Header.objects.get_or_create(
                                date=e.date,
                                parent=user,
                                cid=child,
                                gamekey=e.gamekey,
                                passedlevels=e.passedlevels,
                                repeatedlevels=e.repeatedlevels,
                                playedlevels=e.playedlevels
                            )
                            for l in levels:
                                kwargs = model_to_dict(l)
                                kwargs.pop('headerid')
                                ArbolMusical.objects.get_or_create(header=header, **kwargs)
                    for e in AMH.objects.filter(cid=c.id, parentid=u.id):
                        levels = AML.objects.filter(headerid=e.id)
                        if levels:
                            header, h_created = Header.objects.get_or_create(
                                date=e.date,
                                parent=user,
                                cid=child,
                                gamekey=e.gamekey,
                                gametime=e.gametime,
                                passedlevels=e.passedlevels,
                                repeatedlevels=e.repeatedlevels,
                                playedlevels=e.playedlevels
                            )
                            for l in levels:
                                kwargs = model_to_dict(l)
                                kwargs.pop('headerid')
                                ArenaMagica.objects.get_or_create(header=header, **kwargs)
                    for e in DBH.objects.filter(cid=c.id, parentid=u.id):
                        levels = DBL.objects.filter(headerid=e.id)
                        if levels:
                            header, h_created = Header.objects.get_or_create(
                                date=e.date,
                                parent=user,
                                cid=child,
                                gamekey=e.gamekey,
                                gametime=e.gametime,
                                passedlevels=e.passedlevels,
                                repeatedlevels=e.repeatedlevels,
                                playedlevels=e.playedlevels
                            )
                            for l in levels:
                                kwargs = model_to_dict(l)
                                kwargs.pop('headerid')
                                DondeQuedoLaBolita.objects.get_or_create(header=header, **kwargs)
                    for e in RTH.objects.filter(cid=c.id, parentid=u.id):
                        levels = RTL.objects.filter(headerid=e.id)
                        if levels:
                            header, h_created = Header.objects.get_or_create(
                                date=e.date,
                                parent=user,
                                cid=child,
                                gamekey=e.gamekey,
                                gametime=e.gametime,
                                passedlevels=e.passedlevels,
                                repeatedlevels=e.repeatedlevels,
                                playedlevels=e.playedlevels
                            )
                            for l in levels:
                                kwargs = model_to_dict(l)
                                kwargs.pop('headerid')
                                RecoleccionTesoro.objects.get_or_create(header=header, **kwargs)
                    for e in RH.objects.filter(cid=c.id, parentid=u.id):
                        levels = RL.objects.filter(headerid=e.id)
                        if levels:
                            header, h_created = Header.objects.get_or_create(
                                date=e.date,
                                parent=user,
                                cid=child,
                                gamekey=e.gamekey,
                                gametime=e.gametime,
                                passedlevels=e.passedlevels,
                                repeatedlevels=e.repeatedlevels,
                                playedlevels=e.playedlevels
                            )
                            for l in levels:
                                kwargs = model_to_dict(l)
                                kwargs.pop('headerid')
                                Rio.objects.get_or_create(header=header, **kwargs)
                    for e in SH.objects.filter(cid=c.id, parentid=u.id):
                        levels = SL.objects.filter(headerid=e.id)
                        if levels:
                            header, h_created = Header.objects.get_or_create(
                                date=e.date,
                                parent=user,
                                cid=child,
                                gamekey=e.gamekey,
                                gametime=e.gametime,
                                passedlevels=e.passedlevels,
                                repeatedlevels=e.repeatedlevels,
                                playedlevels=e.playedlevels
                            )
                            for l in levels:
                                kwargs = model_to_dict(l)
                                kwargs.pop('headerid')
                                Sombras.objects.get_or_create(header=header, **kwargs)
                    for t in Ti.objects.filter(parentid=u.id, cid=c.id):
                        ti = TowiIndex.objects.get_or_create(
                            parent=user,
                            cid=child,
                            gamekey=t.gamekey,
                            index=t.index,
                            date=t.date,
                            serverdate=t.serverdate
                        )
                    for ch in CH.objects.filter(parentid=u.id, cid=c.id):
                        cti = ChildrenTowiIsland.objects.create(
                            parent=user,
                            cid=child,
                            kiwis=ch.kiwis,
                            avatar=ch.avatar,
                            avatarclothes=ch.avatarclothes,
                            owneditems=ch.owneditems,
                            activemissions=ch.activemissions,
                            missionlist=ch.missionlist,
                            activeday=ch.activeday,
                            rio_first_time=False,
                            tesoro_first_time=False,
                            arena_first_time=False,
                            sombras_first_time=False,
                            bolita_first_time=False,
                            arbol_first_time=False
                        )
                    for e in PH.objects.filter(cid=c.id, parentid=u.id):
                        levels = PL.objects.filter(header_id=e.id)
                        if levels:
                            header, h_created = Header.objects.get_or_create(
                                date=e.date,
                                parent=user,
                                cid=child,
                                gamekey=e.gamekey,
                                gametime=e.gametime,
                                passedlevels=e.passedlevels,
                                repeatedlevels=e.repeatedlevels,
                                playedlevels=e.playedlevels
                            )
                            for l in levels:
                                try:
                                    kwargs = model_to_dict(l)
                                    kwargs.pop('header_id')
                                    c = Prueba.objects.get_or_create(
                                        header=header,
                                        boarding_age=l.playerage,
                                        boarding_birthday=l.playerbirthday,
                                        boarding_time1=l.inputagetimeofcomp,
                                        boarding_name=l.playername,
                                        boarding_address=l.playeraddress,
                                        boarding_currentdate=l.playercurrentdate,
                                        boarding_time2=l.buytickettimeofcomp,
                                        packforward_score=l.packnormalscore,
                                        packbackward_score=l.packreversescore,
                                        weather_object_packed=l.weatherobjectpacked,
                                        lab1_time=l.lab1time,
                                        lab2_time=l.lab2time,
                                        lab3_time=l.lab3time,
                                        lab1_latency=l.lab1latency,
                                        lab2_latency=l.lab2latency,
                                        lab3_latency=l.lab3latency,
                                        lab1_hits=l.lab1hits,
                                        lab2_hits=l.lab2hits,
                                        lab3_hits=l.lab3hits,
                                        lab1_crosses=l.lab1crosses,
                                        lab2_crosses=l.lab2crosses,
                                        lab3_crosses=l.lab3crosses,
                                        lab1_deadends=l.lab1deadends,
                                        lab2_deadends=l.lab2deadends,
                                        lab3_deadends=l.lab3deadends,
                                        lab_mhits=l.labxhits,
                                        lab_mcrosses=l.labxcrosses,
                                        lab_mdeadends=l.labxdeadends,
                                        lab_time=l.labtimeofcomp,
                                        waitroom_correct=l.waitroomcorrect,
                                        waitroom_incorrect=l.waitroomincorrect,
                                        flyplane_correct=l.flyplanecorrect,
                                        flyplane_incorrect=l.flyplaneincorrect,
                                        flyplane_missed=l.flyplanemissed,
                                        flyplane_greencorrect=l.flyplanegreencorrect,
                                        flyplane_greenincorrect=l.flyplanegreenincorrect,
                                        flyplane_greenmissed=l.flyplanegreenmissed,
                                        flyplane_time=l.flyplanetimeofcomp,
                                        coins_min_correct=l.coinsmincorrect,
                                        coins_min_incorrect=l.coinsminincorrect,
                                        coins_extra_correct=l.coinsextracorrect,
                                        coins_extra_incorrect=l.coinsextraincorrect,
                                        coins_extra_missed=l.coinsextramissed,
                                        coins_selected=l.coinsselected,
                                        coins_pattern_type=l.coinspatterntype,
                                        coins_clickfinish_before_min=l.coinsclicksbeforemin,
                                        coins_time=l.coinstimeofcomp,
                                        unpack_correct=l.unpackfirstcorrect,
                                        arrange1_correct=l.unpacks1correct,
                                        arrange2_correct=l.unpacks2correct,
                                        arrange3_correct=l.unpacks3correct,
                                        arrange1_incorrect=l.unpacks1incorrect,
                                        arrange2_incorrect=l.unpacks2incorrect,
                                        arrange3_incorrect=l.unpacks3incorrect,
                                        arrange1_perseveration=l.unpacks1repeated,
                                        arrange2_perseveration=l.unpacks2repeated,
                                        arrange3_perseveration=l.unpacks3repeated,
                                        arrange_primacy=l.unpackfourfirstsample,
                                        arrange_recence=l.unpackfourlastsample,
                                        arrange_spacialprecision_sample=l.unpackspacialprecisionsample,
                                        arrange_time=l.unpacktimeofcomp,
                                        arrange_perc_correct=l.unpackperctotalcorrect
                                    )
                                except Exception as e:
                                    print(e)
                                    pass
            except Exception as e:
                print('user id {} - {}'.format(u.id, e))
