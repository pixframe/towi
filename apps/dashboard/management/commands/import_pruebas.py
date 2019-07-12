from django.core.management.base import BaseCommand, CommandError
from reusable.models import PruebasLevelsNew, PruebasHeadersNew, Users
from levels.models import Prueba, Header
from reusable.models import Children as OldChildren
from accounts.models import User, Children
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Importa las pruebas de la base vieja a la nueva'

    def add_arguments(self, parser):
        parser.add_argument('date', nargs='+', type=str)

    def handle(self, *args, **options):
        import pudb; pudb.set_trace()
        headers = PruebasHeadersNew.objects.filter(
            date__gte=options['date'][0]
        )
        levels = PruebasLevelsNew.objects.filter(header_id__in=headers)
        for e in headers:
            levels = PruebasLevelsNew.objects.filter(pk=e.id)
            if levels:
                try:
                    old_user = Users.objects.get(pk=e.parentid)
                    user = User.objects.get(email=old_user.email)
                    cid = OldChildren.objects.get(pk=e.cid)
                    children = Children.objects.get(
                        user=user,
                        first_name=cid.name,
                        last_name=cid.lastname
                    )
                    header, h_created = Header.objects.get_or_create(
                        date=e.date,
                        parent=user,
                        cid=children,
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
                            c = Prueba.objects.create(
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
                            print('header y levels creados para {}'.format(user.email))
                        except Exception as e:
                            print(e)
                            pass
                except ObjectDoesNotExist as e:
                    print(e)
                    continue
