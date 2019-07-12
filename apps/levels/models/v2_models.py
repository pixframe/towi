# DJANGO CORE IMPORTS
from django.db import models
from django.utils import timezone
import json

# THIRD PARTY APPS
from multiselectfield import MultiSelectField

# TOWI IMPORTS
from reusable.constants import BLANK, BLANK_NOT_NULL, REQUIRED, BLANK_FALSE
from accounts.models import User, Children
from .v1_models import Header


class ArbolMusicalV2(models.Model):
    header = models.ForeignKey(Header, related_name='arbolMusicalv2', **REQUIRED)
    initial_level = models.IntegerField(**BLANK)
    initial_difficulty = models.IntegerField(**BLANK)
    session_correct_percentage = models.FloatField(**BLANK)
    session_errors_percentage = models.FloatField(**BLANK)
    played_difficulty = models.CharField(max_length=500, **BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    current_level = models.IntegerField(**BLANK)
    current_difficulty = models.IntegerField(**BLANK)
    dad_bird_listened_pre = models.CharField(max_length=500, **BLANK)
    dad_bird_listened_post = models.CharField(max_length=500, **BLANK)
    correct_before_clue = models.CharField(max_length=500, **BLANK)
    errors_before_clue = models.CharField(max_length=500, **BLANK)
    correct_after_clue = models.CharField(max_length=500, **BLANK)
    errors_after_clue = models.CharField(max_length=500, **BLANK)
    total_clues = models.IntegerField(**BLANK)
    total_correct = models.IntegerField(**BLANK)
    total_errors = models.IntegerField(**BLANK)
    essay_time = models.CharField(max_length=500, **BLANK)

    class Meta:
        verbose_name = 'Arbol Musical'


class ArenaMagicaV2(models.Model):
    header = models.ForeignKey(Header, related_name='arenaMagicav2', **REQUIRED)
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


class DondeQuedoLaBolitaV2(models.Model):
    header = models.ForeignKey(Header, related_name='bolitav2', **REQUIRED)
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


class RecoleccionTesoroV2(models.Model):
    header = models.ForeignKey(Header, related_name='tesorov2', **REQUIRED)
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


class RioV2(models.Model):
    header = models.ForeignKey(Header, related_name='riov2', **REQUIRED)
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


class SombrasV2(models.Model):
    header = models.ForeignKey(Header, related_name='sombrasv2', **REQUIRED)
    initial_level = models.IntegerField(**BLANK)
    current_level = models.IntegerField(**BLANK)
    current_difficulty = models.IntegerField(**BLANK)
    session_correct_percentage = models.FloatField(**BLANK)
    session_errors_percentage = models.FloatField(**BLANK)
    played_levels = models.CharField(max_length=500, **BLANK)
    latencies = models.CharField(max_length=500, **BLANK)
    session_time = models.FloatField(**BLANK)

    class Meta:
        verbose_name = 'sombras'


class DataAssesment(models.Model):
    GENDER_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    age = models.IntegerField(**REQUIRED)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, **REQUIRED)
    coins_min_correct = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED, default=0)
    coins_extra_missed = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED, default=0)
    arrange_total_correct = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    arrange_time = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    unpack_correct = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    packforward_score = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    packbackward_score = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    waitroom_correct = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    flyplane_time = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    flyplane_greencorrect = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    flyplane_greenincorrect = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    flyplane_correct = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    flyplane_incorrect = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    lab_hits_sum = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    lab_crosses_sum = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    lab_deadends_sum = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    lab_time_sum = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)
    lab_latency_sum = models.DecimalField(decimal_places=2, max_digits=6, **REQUIRED)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} - {} años'.format(self.gender, self.age)


class Average(DataAssesment):
    class Meta:
        verbose_name = 'Promedio'


class Quartile(DataAssesment):
    number = models.IntegerField(**REQUIRED)

    class Meta:
        verbose_name = 'Cuartil'
        verbose_name_plural = 'Cuartiles'
