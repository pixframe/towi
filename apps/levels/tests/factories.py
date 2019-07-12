import factory

from django.utils import timezone

from ..models import (
    ChildrenTowiIsland,
    Header,
    Prueba,
    ArbolMusicalV2,
    ArenaMagicaV2,
    DondeQuedoLaBolitaV2,
    RioV2,
    SombrasV2,
    RecoleccionTesoroV2,
)
from accounts.tests.factories import UserFactory, ChildrenFactory


class ChildrenTowiIslandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChildrenTowiIsland

    parent = factory.SubFactory(UserFactory)
    cid = factory.SubFactory(ChildrenFactory)
    kiwis = 0
    activeday = 0
    date = factory.Faker('date_time')
    session_date = factory.Faker('date')


class HeaderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Header

    date = factory.Faker('date_time')
    parent = factory.SubFactory(UserFactory)
    cid = factory.SubFactory(ChildrenFactory)
    gametime = factory.Faker('random_number')
    device = 'ios'
    version = '1.0'
    passedlevels = 10
    repeatedlevels = 2
    playedlevels = 12


class HeaderPruebaFactory(HeaderFactory):
    gamekey = 'PruebaEcologica'


class HeaderArbolFactory(HeaderFactory):
    gamekey = 'ArbolMusical'


class HeaderArenaFactory(HeaderFactory):
    gamekey = 'ArenaMagica'


class HeaderRioFactory(HeaderFactory):
    gamekey = 'Rio'


class HeaderTesoroFactory(HeaderFactory):
    gamekey = 'Tesoro'


class HeaderSombrasFactory(HeaderFactory):
    gamekey = 'JuegoDeSombras'


class HeaderMonosFactory(HeaderFactory):
    gamekey = 'DondeQuedoLaBolita'


class ArbolMusicalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ArbolMusicalV2

    header = factory.SubFactory(HeaderArbolFactory)
    initial_level = 10
    initial_difficulty = 10
    session_correct_percentage = 10.10
    session_errors_percentage = 10.10
    played_difficulty = 'texto'
    played_levels = 'texto'
    current_level = 10
    current_difficulty = 10
    dad_bird_listened_pre = 'texto'
    dad_bird_listened_post = 'texto'
    correct_before_clue = 'texto'
    errors_before_clue = 'texto'
    correct_after_clue = 'texto'
    errors_after_clue = 'texto'
    total_clues = 10
    total_correct = 10
    total_errors = 10
    essay_time = 'texto'


class ArenaMagicaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ArenaMagicaV2

    header = factory.SubFactory(HeaderArenaFactory)
    initial_level_motor = 10
    initial_level_overlapping = 10
    initial_level_clousre = 10
    current_level = 10
    current_level_motor = 10
    current_level_overlapping = 10
    current_level_clousre = 10
    session_number = 10
    session_overdraw_percentage = 10.10
    session_accuracy_percentage = 10.10
    types_levels = 'texto'
    played_levels = 'texto'
    time_percentage = 'texto'
    accuracy = 'texto'
    overdraw = 'texto'
    change_level_motor = 10
    change_level_overlapping = 10
    change_level_clousure = 10


class MonosTraviesosFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DondeQuedoLaBolitaV2

    header = factory.SubFactory(HeaderMonosFactory)
    initial_level = 10
    initial_difficulty = 10
    current_level = 10
    current_difficulty = 10
    session_number = 10
    session_correct_percentage = 10.10
    session_errors_percentage = 10.10
    played_levels = 'texto'
    played_difficulty = 'texto'
    session_time = 10.10
    correct_monkeys = 10
    errors_monkeys = 10
    latency = 'texto'


class TesoroFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RecoleccionTesoroV2

    header = factory.SubFactory(HeaderTesoroFactory)
    initial_level = 10
    initial_difficulty = 10
    current_level = 10
    current_difficulty = 10
    session_correct_total = 10
    session_errors_total = 10
    total_second_chances = 10
    diffrence_in_quantity = 10
    played_levels = 'texto'
    played_difficulty = 'texto'
    session_minobjects = 10
    session_maxobjects = 10
    session_time = 10.10
    requestreminder = 10


class RioFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RioV2

    header = factory.SubFactory(HeaderRioFactory)
    initial_level = 10
    initial_difficulty = 10
    current_level = 10
    current_difficulty = 10
    session_correct_total = 10
    session_errors_total = 10
    played_levels = 'texto'
    played_difficulty = 'texto'
    target_total = 10
    target_correct = 10
    target_errors = 10


class SombrasFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SombrasV2

    header = factory.SubFactory(HeaderSombrasFactory)
    initial_level = 10
    initial_difficulty = 10
    current_level = 10
    current_difficulty = 10
    session_correct_percentage = 10.10
    session_errors_percentage = 10.10
    played_levels = 'texto'
    latencies = 'texto'
    session_time = 10.10


class PruebaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Prueba

    header = factory.SubFactory(HeaderPruebaFactory)
    # BOARDING MINI GAME
    boarding_latency = 10.0
    boarding_age = 10
    boarding_birthday = '7 dic'
    boarding_time1 = 10
    boarding_name = factory.Faker('name')
    boarding_address = factory.Faker('address')
    boarding_currentdate = 'hoy'
    boarding_time2 = 10
    #
    packforward_tutorial = 10
    packforward_time = 10.10
    packforward_incorrect_secuence = 10
    packforward_instrusions = 10
    packbackward_tutorial = 10
    packforward_score = 10
    packbackward_score = 1
    packbackward_time = 10.10
    packbackward_incorrect_secuence = 10
    packbackward_intrusions = 10
# WHEATER MINI GAME
    weather_latency = 10.01
    weather_object_packed = 'todos'
    weather_time = 1.5
    #
    lab_start_level = 10
    lab1_time = 10.10
    lab2_time = 10.10
    lab3_time = 10.10
    lab1_latency = 10.10
    lab2_latency = 10.10
    lab3_latency = 10.10
    lab1_hits = 2
    lab2_hits = 2
    lab3_hits = 2
    lab1_crosses = 2
    lab2_crosses = 2
    lab3_crosses = 2
    lab1_deadends = 2
    lab2_deadends = 2
    lab3_deadends = 2
    lab1_changeofroutes = 2
    lab2_changeofroutes = 5
    lab3_changeofroutes = 6
    lab_mhits = 10.10
    lab_mcrosses = 10.10
    lab_mdeadends = 10.10
    lab_time = 5
    # WAITROOM MINI GAMEi
    waitroom_correct = 10
    waitroom_incorrect = 10
    waitroom_correct_mlatency = 12.2
    waitroom_incorrect_mlatency = 12.2
    waitroom_tutorial = 10
    flyplane_tutorial = 10
    flyplane_series = 10
    flyplane_correct = 10
    flyplane_incorrect = 10
    flyplane_missed = 10
    flyplane_greencorrect = 10
    flyplane_greenincorrect = 10
    flyplane_greenmissed = 10
    flyplane_time = 10
    flyplane_correct_mlatency = 10.10
    flyplane_incorrect_mlatency = 10.10
    flyplane_greencorrect_mlatency = 10.10
    flyplane_greenincorrect_mlatency =10.10
    #
    coins_tutorial = 10
    coins_level = 10
    coins_min_correct = 10
    coins_min_incorrect = 10
    coins_extra_correct = 10
    coins_extra_incorrect = 10
    coins_extra_missed = 10
    coins_correct_mlatency = 10.10
    coins_incorrect_mlatency = 10.10
    coins_selected = 'TEXTO'
    coins_pattern_type = 1
    coins_organization_score = 10
    coins_clickfinish_before_min =10
    coins_time = 10
    #
    unpack_correct = 10
    unpack_incorrect = 10
    unpack_perseveration = 10
    unpack_first_selected = 'texto'
    unpack_first_correct = 'texto'
    unpack_bad_recognition = 10
    unpack_time = 10
    # ARRANGE MINI GAME
    arrange_amplitude = 12
    arrange1_correct = 10
    arrange2_correct = 10
    arrange3_correct = 10
    arrange1_incorrect = 10
    arrange2_incorrect = 10
    arrange3_incorrect = 10
    arrange1_perseveration = 10
    arrange2_perseveration = 10
    arrange3_perseveration = 10
    arrange_learningcurve = 10
    arrange_primacy = 'texto'
    arrange_recence = 'texto'
    arrange_spacialprecision_score = 'texto'
    arrange_spacialprecision_sample = 'texto'
    arrange_storage_efficency1 = 10
    arrange_storage_efficency2 = 10
    arrange_incorrect_repeated = 'texto'
    arrange_correct_mlatency = 10.10
    arrange_incorrect_mlatency = 10.10
    arrange_time = 10
    arrange_perc_correct = 10.10
    total_time = 10.10
