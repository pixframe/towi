from decimal import Decimal

# DJANGO CORE IMPORTS
from django.db import models
from django.utils import timezone
import json

# THIRD PARTY APPS
from multiselectfield import MultiSelectField

# TOWI IMPORTS
from reusable.constants import BLANK, BLANK_NOT_NULL, REQUIRED, BLANK_FALSE
from accounts.models import User, Children


GAME_KEYS = (
    ('ArbolMusical', 'ArbolMusical'),
    ('Rio', 'Rio'),
    ('ArenaMagica', 'ArenaMagica'),
    ('DondeQuedoLaBolita', 'DondeQuedoLaBolita'),
    ('Tesoro', 'Tesoro'),
    ('JuegoDeSombras', 'JuegoDeSombras'),
    ('PruebaEcologica', 'PruebaEcologica')
)

LEVELS_KEYS_CHOICES = (
    ('ArbolMusical', 'ArbolMusical'),
    ('Rio', 'Rio'),
    ('ArenaMagica', 'ArenaMagica'),
    ('DondeQuedoLaBolita', 'DondeQuedoLaBolita'),
    ('Tesoro', 'Tesoro'),
    ('JuegoDeSombras', 'JuegoDeSombras'),
)


class Header(models.Model):
    date = models.DateTimeField(blank=False, null=False)
    parent = models.ForeignKey(User, related_name='headers', **REQUIRED)
    cid = models.ForeignKey(Children, related_name='headers', **REQUIRED)
    gamekey = models.CharField(max_length=100, choices=GAME_KEYS)
    gametime = models.IntegerField(**BLANK)
    passedlevels = models.PositiveSmallIntegerField(**BLANK)
    repeatedlevels = models.PositiveSmallIntegerField(**BLANK)
    playedlevels = models.PositiveSmallIntegerField(**BLANK)
    device = models.CharField(max_length=400, **BLANK)
    version = models.CharField(max_length=200, **BLANK_NOT_NULL)
    application_number = models.IntegerField(**BLANK)
    total_sessions = models.IntegerField(**BLANK)
    total_time = models.FloatField(**BLANK)
    last_session_date = models.DateTimeField(**BLANK)
    game_frequency = models.FloatField(**BLANK)
    totalcorrect_percentage = models.FloatField(**BLANK)
    totalerrors_average = models.FloatField(**BLANK)

    class Meta:
        verbose_name = 'Header'
        ordering = ('id', )

    def __str__(self):
        return '{} - {}'.format(self.parent.email, self.cid.get_full_name)

    @property
    def time_played(self):
        time = 0
        for am in ArbolMusical.objects.filter(headerid=self.id):
            time += am.time
        return round(time / 60)


class ArbolMusical(models.Model):
    header = models.ForeignKey(Header, related_name='arbolMusical', **REQUIRED)
    birds = models.PositiveSmallIntegerField(**BLANK_FALSE)
    nests = models.PositiveSmallIntegerField(**BLANK)
    level = models.PositiveSmallIntegerField(**BLANK)
    sublevel = models.PositiveSmallIntegerField(**BLANK)
    tutorial = models.PositiveSmallIntegerField(**BLANK)
    sound = models.CharField(max_length=500, **BLANK)
    birdsound = models.CharField(max_length=500, **BLANK)
    time = models.PositiveSmallIntegerField(**BLANK)
    birdlistenedpre = models.CharField(max_length=500, **BLANK)
    birdlistened = models.CharField(max_length=500, **BLANK)
    errors = models.PositiveSmallIntegerField(**BLANK)
    correct = models.PositiveSmallIntegerField(**BLANK)
    initial_level = models.IntegerField(**BLANK)
    initial_difficulty = models.IntegerField(**BLANK)
    session_correct_percentage = models.FloatField(**BLANK)
    session_errors_percentage = models.FloatField(**BLANK)
    played_difficulty = models.CharField(max_length=500, **BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    final_Level = models.IntegerField(**BLANK)
    final_Difficulty = models.IntegerField(**BLANK)
    dad_bird_listened_pre = models.CharField(max_length=500, **BLANK)
    dad_bird_listened_post = models.CharField(max_length=500, **BLANK)
    correct_before_clue = models.CharField(max_length=500, **BLANK)
    errors_before_clue = models.CharField(max_length=500, **BLANK)
    correct_after_clue = models.CharField(max_length=500, **BLANK)
    errors_after_clue = models.CharField(max_length=500, **BLANK)
    total_clues = models.CharField(max_length=500, **BLANK)
    total_correct = models.CharField(max_length=500, **BLANK)
    total_errors = models.CharField(max_length=500, **BLANK)
    essay_time = models.CharField(max_length=500, **BLANK)

    class Meta:
        verbose_name = 'Arbol Musical'


class ArenaMagica(models.Model):
    header = models.ForeignKey(Header, related_name='arenaMagica', **REQUIRED)
    levelkey = models.CharField(max_length=100, choices=GAME_KEYS)
    level = models.PositiveSmallIntegerField(**BLANK)
    sublevel = models.PositiveSmallIntegerField(**BLANK)
    sublevel2 = models.PositiveSmallIntegerField(**BLANK)
    sublevel3 = models.PositiveSmallIntegerField(**BLANK)
    time = models.PositiveSmallIntegerField(**BLANK)
    passed = models.PositiveSmallIntegerField(**BLANK)
    repeated = models.PositiveSmallIntegerField(**BLANK)
    accuracy = models.PositiveSmallIntegerField(**BLANK)
    initial_level_motor = models.PositiveSmallIntegerField(**BLANK)
    initial_level_overlapping = models.PositiveSmallIntegerField(**BLANK)
    initial_level_clousre = models.PositiveSmallIntegerField(**BLANK)
    current_level = models.PositiveSmallIntegerField(**BLANK)
    current_level_motor = models.PositiveSmallIntegerField(**BLANK)
    current_level_overlapping = models.PositiveSmallIntegerField(**BLANK)
    current_level_clousre = models.PositiveSmallIntegerField(**BLANK)
    session_number = models.PositiveSmallIntegerField(**BLANK)
    session_overdraw_percentage = models.FloatField(**BLANK)
    session_accuracy_percentage = models.FloatField(**BLANK)
    types_levels = models.CharField(max_length=500, **BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    time_percentage = models.CharField(max_length=500, **BLANK)
    accuracy = models.CharField(max_length=500, **BLANK)
    overdraw = models.CharField(max_length=500, **BLANK)
    change_level_motor = models.PositiveSmallIntegerField(**BLANK)
    change_level_overlapping = models.PositiveSmallIntegerField(**BLANK)
    change_level_clousure = models.PositiveSmallIntegerField(**BLANK)

    class Meta:
        verbose_name = 'Arena Mágica'


class DondeQuedoLaBolita(models.Model):
    header = models.ForeignKey(Header, related_name='bolita', **REQUIRED)
    levelkey = models.CharField(max_length=100, choices=GAME_KEYS)
    level = models.PositiveSmallIntegerField(**BLANK)
    sublevel = models.PositiveSmallIntegerField(**BLANK)
    time = models.PositiveSmallIntegerField(**BLANK)
    numofmonkeys = models.PositiveSmallIntegerField(**BLANK)
    numofobjects = models.PositiveSmallIntegerField(**BLANK)
    instructions = models.CharField(max_length=500, **BLANK)
    numofmovements = models.PositiveSmallIntegerField(**BLANK)
    timeofmovements = models.CharField(max_length=100, **BLANK)
    correct = models.PositiveSmallIntegerField(**BLANK)
    initial_level = models.PositiveSmallIntegerField(**BLANK)
    initial_difficulty = models.PositiveSmallIntegerField(**BLANK)
    current_level = models.PositiveSmallIntegerField(**BLANK)
    current_difficulty = models.PositiveSmallIntegerField(**BLANK)
    session_number = models.PositiveSmallIntegerField(**BLANK)
    session_correct_percentage = models.FloatField(**BLANK)
    session_errors_percentage = models.FloatField(**BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    played_difficulty = models.CharField(max_length=500, **BLANK)
    session_time = models.FloatField(**BLANK)
    correct_monkeys = models.PositiveSmallIntegerField(**BLANK)
    errors_monkeys = models.PositiveSmallIntegerField(**BLANK)
    latency = models.CharField(max_length=500, **BLANK)

    class Meta:
        verbose_name = 'Donde quedo la bolita'


class GameAreas(models.Model):
    game_id = models.IntegerField(**BLANK)
    area = models.IntegerField(**BLANK)
    subarea = models.IntegerField(**BLANK)

    class Meta:
        verbose_name = 'Game areas'


class GamesConfiguration(models.Model):
    cid = models.ForeignKey(Children, related_name='games_configurations')
    configid = models.IntegerField(**BLANK)
    sid = models.IntegerField(**BLANK)
    date = models.DateTimeField(**BLANK)

    class Meta:
        verbose_name = 'Game Configuration'


class GamesConfigurationFiles(models.Model):
    cid = models.ForeignKey(Children, related_name='games_configurations_files')
    gamekey = models.CharField(max_length=100, choices=GAME_KEYS)
    name = models.CharField(max_length=100, **BLANK)
    description = models.CharField(max_length=1000, **BLANK)
    file = models.CharField(max_length=100, **BLANK)
    date = models.DateTimeField(**BLANK)

    class Meta:
        verbose_name = 'Game Configuration Files'


class Prueba(models.Model):
    header = models.ForeignKey(Header, related_name='pruebaEcologica', **REQUIRED)
    # BOARDING MINI GAME
    boarding_latency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    boarding_age = models.IntegerField(db_column='playerAge')
    boarding_birthday = models.CharField(db_column='playerBirthday', max_length=300)
    boarding_time1 = models.IntegerField(db_column='inputAgeTimeOfComp')
    boarding_name = models.CharField(db_column='playerName', max_length=300)
    boarding_address = models.CharField(db_column='playerAddress', max_length=300)
    boarding_currentdate = models.CharField(db_column='playerCurrentDate', max_length=300)
    boarding_time2 = models.IntegerField(db_column='buyTicketTimeOfComp')
    # PACK BACKWARD MINI GAME
    packforward_tutorial = models.IntegerField(**BLANK)
    packforward_time = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    packforward_incorrect_secuence = models.IntegerField(**BLANK)
    packforward_instrusions = models.IntegerField(**BLANK)
    packbackward_tutorial = models.IntegerField(**BLANK)
    packforward_score = models.IntegerField(db_column='packNormalScore')
    packbackward_score = models.IntegerField(db_column='packReverseScore')
    packbackward_time = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    packbackward_incorrect_secuence = models.IntegerField(**BLANK)
    packbackward_intrusions = models.IntegerField(**BLANK)
    # WHEATER MINI GAME
    weather_latency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    weather_object_packed = models.CharField(db_column='weatherObjectPacked', max_length=1000, **BLANK)
    weather_time = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    # DRIVE TO AIRPORT TUTORIAL
    lab_start_level = models.IntegerField(**BLANK)
    lab1_time = models.FloatField(db_column='lab1Time')
    lab2_time = models.FloatField(db_column='lab2Time')
    lab3_time = models.FloatField(db_column='lab3Time')
    lab1_latency = models.FloatField(db_column='lab1Latency')
    lab2_latency = models.FloatField(db_column='lab2Latency')
    lab3_latency = models.FloatField(db_column='lab3Latency')
    lab1_hits = models.IntegerField(db_column='lab1Hits')
    lab2_hits = models.IntegerField(db_column='lab2Hits')
    lab3_hits = models.IntegerField(db_column='lab3Hits')
    lab1_crosses = models.IntegerField(db_column='lab1Crosses')
    lab2_crosses = models.IntegerField(db_column='lab2Crosses')
    lab3_crosses = models.IntegerField(db_column='lab3Crosses')
    lab1_deadends = models.IntegerField(db_column='lab1DeadEnds')
    lab2_deadends = models.IntegerField(db_column='lab2DeadEnds')
    lab3_deadends = models.IntegerField(db_column='lab3DeadEnds')
    lab1_changeofroutes = models.IntegerField(**BLANK)
    lab2_changeofroutes = models.IntegerField(**BLANK)
    lab3_changeofroutes = models.IntegerField(**BLANK)
    lab_mhits = models.DecimalField(db_column='labXHits', max_digits=6, decimal_places=2, **BLANK)
    lab_mcrosses = models.DecimalField(db_column='labXCrosses', max_digits=6, decimal_places=2, **BLANK)
    lab_mdeadends = models.DecimalField(db_column='labXDeadEnds', max_digits=6, decimal_places=2, **BLANK)
    lab_time = models.IntegerField(db_column='labTimeOfComp')
    # WAITROOM MINI GAME
    waitroom_correct = models.IntegerField(db_column='waitRoomCorrect')
    waitroom_incorrect = models.IntegerField(db_column='waitRoomIncorrect')
    waitroom_correct_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    waitroom_incorrect_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    waitroom_tutorial = models.IntegerField(**BLANK)
    flyplane_tutorial = models.IntegerField(**BLANK)
    flyplane_series = models.IntegerField(**BLANK)
    flyplane_correct = models.IntegerField(db_column='flyPlaneCorrect')
    flyplane_incorrect = models.IntegerField(db_column='flyPlaneIncorrect')
    flyplane_missed = models.IntegerField(db_column='flyPlaneMissed')
    flyplane_greencorrect = models.IntegerField(db_column='flyPlaneGreenCorrect')
    flyplane_greenincorrect = models.IntegerField(db_column='flyPlaneGreenIncorrect')
    flyplane_greenmissed = models.IntegerField(db_column='flyPlaneGreenMissed')
    flyplane_time = models.IntegerField(db_column='flyPlaneTimeOfComp')
    flyplane_correct_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    flyplane_incorrect_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    flyplane_greencorrect_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    flyplane_greenincorrect_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    # COINS MINI GAME
    coins_tutorial = models.IntegerField(**BLANK)
    coins_level = models.IntegerField(**BLANK)
    coins_min_correct = models.IntegerField(db_column='coinsMinCorrect')
    coins_min_incorrect = models.IntegerField(db_column='coinsMinIncorrect')
    coins_extra_correct = models.IntegerField(db_column='coinsExtraCorrect')
    coins_extra_incorrect = models.IntegerField(db_column='coinsExtraIncorrect')
    coins_extra_missed = models.IntegerField(db_column='coinsExtraMissed')
    coins_correct_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    coins_incorrect_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    coins_selected = models.CharField(db_column='coinsSelected', max_length=1000)
    coins_pattern_type = models.IntegerField(db_column='coinsPatternType', **BLANK)  # documental db
    coins_organization_score = models.IntegerField(**BLANK)
    coins_clickfinish_before_min = models.IntegerField(db_column='coinsClicksBeforeMin')
    coins_time = models.IntegerField(db_column='coinsTimeOfComp')
    # UNPACK MINIGAME
    unpack_correct = models.IntegerField(db_column='unPackFirstCorrect')
    unpack_incorrect = models.IntegerField(**BLANK)
    unpack_perseveration = models.IntegerField(**BLANK)
    unpack_first_selected = models.CharField(max_length=300, **BLANK_NOT_NULL)
    unpack_first_correct = models.CharField(max_length=300, **BLANK_NOT_NULL)
    unpack_bad_recognition = models.IntegerField(**BLANK)
    unpack_time = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    # ARRANGE MINI GAME
    arrange_amplitude = models.IntegerField(**BLANK, default=0)
    arrange1_correct = models.IntegerField(db_column='unPackS1Correct')
    arrange2_correct = models.IntegerField(db_column='unPackS2Correct')
    arrange3_correct = models.IntegerField(db_column='unPackS3Correct')
    arrange1_incorrect = models.IntegerField(db_column='unPackS1Incorrect')
    arrange2_incorrect = models.IntegerField(db_column='unPackS2Incorrect')
    arrange3_incorrect = models.IntegerField(db_column='unPackS3Incorrect')
    arrange1_perseveration = models.IntegerField(db_column='unPackS1Repeated')
    arrange2_perseveration = models.IntegerField(db_column='unPackS2Repeated')
    arrange3_perseveration = models.IntegerField(db_column='unPackS3Repeated')
    arrange_learningcurve = models.IntegerField(**BLANK)
    arrange_primacy = models.CharField(db_column='unPackFourFirstSample', max_length=1000)
    arrange_recence = models.CharField(db_column='unPackFourLastSample', max_length=1000)
    arrange_spacialprecision_score = models.CharField(max_length=200, **BLANK)
    arrange_spacialprecision_sample = models.CharField(db_column='unPackSpacialPrecisionSample', max_length=1000)
    arrange_storage_efficency1 = models.IntegerField(**BLANK)
    arrange_storage_efficency2 = models.IntegerField(**BLANK)
    arrange_incorrect_repeated = models.CharField(max_length=300, **BLANK_NOT_NULL)
    arrange_correct_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    arrange_incorrect_mlatency = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)
    arrange_time = models.IntegerField(db_column='unPackTimeOfComp')
    arrange_perc_correct = models.DecimalField(db_column='unPackPercTotalCorrect', max_digits=6, decimal_places=2, **BLANK)
    total_time = models.DecimalField(max_digits=10, decimal_places=4, **BLANK)

    class Meta:
        verbose_name = 'Pruebas'

    @property
    def changeofroutes_sum(self):
        try:
            value = self.lab1_changeofroutes + self.lab2_changeofroutes + self.lab3_changeofroutes
        except Exception as e:
            return 'Sin valor'
        return value

    @property
    def coins_omision(self):
        try:
            value = self.coins_level - self.coins_min_correct
        except Exception as e:
            value = 'Sin valor'
        return value

    @property
    def lab_hits_sum(self):
        value = self.lab1_hits + self.lab2_hits + self.lab3_hits
        return value

    @property
    def lab_crosses_sum(self):
        value = self.lab1_crosses + self.lab2_crosses + self.lab3_crosses
        return value

    @property
    def lab_deadends_sum(self):
        value = self.lab1_deadends + self.lab2_deadends + self.lab3_deadends
        return value

    @property
    def arrange_correct_sum(self):
        value = self.arrange1_correct + self.arrange2_correct + self.arrange3_correct
        return value

    @property
    def arrange_incorrect_sum(self):
        value = self.arrange1_incorrect + self.arrange2_incorrect + self.arrange3_incorrect
        return value

    @property
    def lab_latency_sum(self):
        value = self.lab1_latency + self.lab2_latency + self.lab3_latency
        return value

    @property
    def lab_time_sum(self):
        value = self.lab1_time + self.lab2_time + self.lab3_time
        return value

    @property
    def weather_election_type(self):
        value = self.weather_object_packed
        if value in ['', None]:
            value = 'sombrillacerrada,guantes'
        if value == 'sombrillacerrada,':
            return 'Congruente'
        elif not 'sombrilla' in value:
            return 'Incogruente'
        else:
            return 'Ambiguo'

    @property
    def waitroom_omision(self):
        return 11 - self.waitroom_correct

    @property
    def arrange_perseveration_sum(self):
        try:
            value = self.arrange1_perseveration + self.arrange2_perseveration + self.arrange3_perseveration
            return value
        except Exception as e:
            return 'Sin valor'

    @property
    def arrange_total_correct(self):
        val = self.arrange_correct_sum / 3        
        try:
            val = val / self.arrange_amplitude            
        except:
            val = float(0)
        val = val * 100
        return round(val, 2)

    @property
    def total_arrange_amplitude(self):
        if self.arrange_amplitude is None:
            return 0 * 3
        return self.arrange_amplitude * 3
        
    @property
    def coins_selected_json(self):
        value = json.loads(self.coins_selected)
        return value
    
    @property
    def weather_object_packed_format(self):
        values = self.weather_object_packed
        new_values = values.replace('sombrillacerrada', 'paraguas')
        return new_values

class RecoleccionTesoro(models.Model):
    header = models.ForeignKey(Header, related_name='tesoro', **REQUIRED)
    level = models.IntegerField(**BLANK)
    sublevel = models.IntegerField(**BLANK)
    time = models.IntegerField(**BLANK)
    tutorial = models.IntegerField(**BLANK)
    passed = models.IntegerField(**BLANK)
    playerobjects = models.CharField(db_column='playerObjects', max_length=500, **BLANK)
    playerobjectsquantity = models.CharField(db_column='playerObjectsQuantity', max_length=500, **BLANK)
    correctobjects = models.CharField(db_column='correctObjects', max_length=500, **BLANK)
    correctobjectsquantity = models.CharField(db_column='correctObjectsQuantity', max_length=500, **BLANK)
    spawnedobjects = models.CharField(db_column='spawnedObjects', max_length=500, **BLANK)
    spawneddistractors = models.CharField(db_column='spawnedDistractors', max_length=500, **BLANK)
    notsurecorrect = models.IntegerField(db_column='notSureCorrect', **BLANK)
    notsureincorrect = models.IntegerField(db_column='notSureIncorrect', **BLANK)
    minobjects = models.IntegerField(db_column='minObjects', **BLANK)
    maxobjects = models.IntegerField(db_column='maxObjects', **BLANK)
    availableobjects = models.CharField(db_column='availableObjects', max_length=500, **BLANK)
    availablecategories = models.CharField(db_column='availableCategories', max_length=500, **BLANK)
    searchorders = models.CharField(db_column='searchOrders', max_length=500, **BLANK)
    availabledistractors = models.CharField(db_column='availableDistractors', max_length=500, **BLANK)
    initial_level = models.IntegerField(**BLANK)
    initial_difficulty = models.IntegerField(**BLANK)
    current_level = models.IntegerField(**BLANK)
    current_difficulty = models.IntegerField(**BLANK)
    session_correct_total = models.IntegerField(**BLANK)
    session_errors_total = models.IntegerField(**BLANK)
    total_second_chances = models.IntegerField(**BLANK)
    diffrence_in_quantity = models.IntegerField(**BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    played_difficulty = models.CharField(max_length=500, **BLANK)
    session_minobjects = models.IntegerField(**BLANK)
    session_maxobjects = models.IntegerField(**BLANK)
    session_time = models.FloatField(**BLANK)
    requestreminder = models.IntegerField(**BLANK)

    class Meta:
        verbose_name = 'Tesoro'


class Rio(models.Model):
    header = models.ForeignKey(Header, related_name='rio', **REQUIRED)
    level = models.IntegerField(**BLANK)
    sublevel = models.IntegerField(**BLANK)
    time = models.IntegerField(**BLANK)
    tutorial = models.IntegerField(**BLANK)
    reverse = models.IntegerField(**BLANK)
    speed = models.IntegerField(**BLANK)
    correctobjects = models.IntegerField(db_column='correctObjects', **BLANK)
    incorrectobjects = models.IntegerField(db_column='incorrectObjects', **BLANK)
    levelobjects = models.CharField(db_column='levelObjects', max_length=500, **BLANK)
    availableobjects = models.CharField(db_column='availableObjects', max_length=500, **BLANK)
    reverseobjects = models.CharField(db_column='reverseObjects', max_length=500, **BLANK)
    neutralobjects = models.CharField(db_column='neutralObjects', max_length=500, **BLANK)
    forceforestobjects = models.CharField(db_column='forceForestObjects', max_length=500, **BLANK)
    forcebeachforest = models.CharField(db_column='forceBeachForest', max_length=500, **BLANK)
    specialreverseobjects = models.CharField(db_column='specialReverseObjects', max_length=500, **BLANK)
    specialleaveobjects = models.CharField(db_column='specialLeaveObjects', max_length=500, **BLANK)
    initial_level = models.IntegerField(**BLANK)
    initial_difficulty = models.IntegerField(**BLANK)
    current_level = models.IntegerField(**BLANK)
    current_difficulty = models.IntegerField(**BLANK)
    session_correct_total = models.IntegerField(**BLANK)
    session_errors_total = models.IntegerField(**BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    played_difficulty = models.CharField(max_length=500, **BLANK)
    target_total = models.IntegerField(**BLANK)
    target_correct = models.IntegerField(**BLANK)
    target_errors = models.IntegerField(**BLANK)

    class Meta:
        verbose_name = 'Rio'


class Sombras(models.Model):
    header = models.ForeignKey(Header, related_name='sombras', **REQUIRED)
    levelkey = models.CharField(db_column='levelKey', max_length=100, **BLANK)
    level = models.IntegerField(**BLANK)
    sublevel = models.IntegerField(**BLANK)
    shadow = models.CharField(max_length=100, **BLANK)
    shadowtime = models.CharField(db_column='shadowTime', max_length=100, **BLANK)
    numofoptions = models.IntegerField(db_column='numOfOptions')
    options = models.CharField(max_length=500, **BLANK)
    correct = models.IntegerField(**BLANK)
    time = models.IntegerField(**BLANK)
    initial_level = models.IntegerField(**BLANK)
    current_level = models.IntegerField(**BLANK)
    sessioncorrect_percentage = models.FloatField(**BLANK)
    sessionerrors_percentage = models.FloatField(**BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    latencies = models.CharField(max_length=500, **BLANK)
    session_time = models.FloatField(**BLANK)

    class Meta:
        verbose_name = 'sombras'


class ChildrenTowiIsland(models.Model):
    parent = models.ForeignKey(User, related_name='towiIsland')
    cid = models.ForeignKey(Children, related_name='towiIslandChild')
    kiwis = models.IntegerField(**BLANK)
    avatar = models.CharField(max_length=100, **BLANK)
    avatarclothes = models.CharField(db_column='avatarClothes', max_length=1000, **BLANK)
    owneditems = models.CharField(db_column='ownedItems', max_length=1000, **BLANK)
    activemissions = models.CharField(db_column='activeMissions', max_length=1000, **BLANK)
    order_missions = models.IntegerField(**BLANK)
    missionlist = models.CharField(db_column='missionList', max_length=1000, **BLANK)
    activeday = models.IntegerField(db_column='activeDay')
    rio_first_time = models.BooleanField(default=True, db_column='rioTutorial')
    tesoro_first_time = models.BooleanField(default=True, db_column='arbolMusicalTutorial')
    arena_first_time = models.BooleanField(default=True)
    sombras_first_time = models.BooleanField(default=True)
    bolita_first_time = models.BooleanField(default=True)
    arbol_first_time = models.BooleanField(default=True)
    rio_level_set = models.BooleanField(default=False)
    tesoro_level_set = models.BooleanField(default=False)
    arbol_level_set = models.BooleanField(default=False)
    arena_level_set = models.BooleanField(default=False)
    arena_level_set2 = models.BooleanField(default=False)
    sombras_level_set = models.BooleanField(default=False)
    bolita_level_set = models.BooleanField(default=False)
    island_shopping_list = models.CharField(max_length=200, **BLANK)
    date = models.DateTimeField(**BLANK)
    session_date = models.DateField(**REQUIRED)

    class Meta:
        verbose_name = 'Towi Island'

    def first_time_completed(self):
        if self.rio_first_time is False and \
         self.tesoro_first_time is False and \
         self.arbol_first_time is False and \
         self.arena_first_time is False and \
         self.sombras_first_time is False and \
         self.bolita_first_time is False:
            return True
        else:
            return False

    @classmethod
    def create_towi_island(cls, user, children):
        instance = cls.objects.create(
            parent=user,
            cid=children,
            kiwis=0,
            activeday=0,
            date=timezone.now(),
            session_date=timezone.now().date()
        )
        try:
            instance.activemissions = Session.objects.get(order=0).games
            instance.order_missions = Session.objects.get(order=0).order
            instance.save()
        except Exception as e:
            pass
        return instance


class TowiIndex(models.Model):
    parent = models.ForeignKey(User, related_name='towiIndex')
    cid = models.ForeignKey(Children, related_name='towiIndexChild')
    gamekey = models.CharField(max_length=100, choices=GAME_KEYS)
    index = models.FloatField(**BLANK)
    date = models.DateTimeField(**BLANK)
    serverdate = models.DateTimeField(db_column='serverDate')

    class Meta:
        verbose_name = 'Towi index'


class PixframeCardsCodes(models.Model):
    code = models.CharField(max_length=100, **BLANK)
    used = models.IntegerField(**BLANK)
    temp = models.IntegerField(**BLANK)
    temp_num = models.IntegerField(**BLANK)
    activation_day = models.DateField(**BLANK)

    class Meta:
        verbose_name = 'Pixframe cards code'


class Session(models.Model):
    name = models.CharField(max_length=50, **BLANK_NOT_NULL)
    games = MultiSelectField(choices=LEVELS_KEYS_CHOICES, max_choices=6)
    order = models.PositiveSmallIntegerField(**REQUIRED)
    children = models.ManyToManyField(Children, related_name='sessions', blank=True)

    class Meta:
        verbose_name = 'Sesiones de juego'
        verbose_name_plural = 'Sesiones de juego'
        ordering = ('order', )

    def __str__(self):
        return self.name
