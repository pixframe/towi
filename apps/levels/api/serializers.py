# Third-party Libraries
from rest_framework import serializers

# Own´s Libraries
from ..models import (
    Prueba,
    Header,
    ArbolMusical,
    ArenaMagica,
    DondeQuedoLaBolita,
    Rio,
    RecoleccionTesoro,
    Sombras,
    ArbolMusicalV2,
    ArenaMagicaV2,
    DondeQuedoLaBolitaV2,
    RioV2,
    RecoleccionTesoroV2,
    SombrasV2,
)

from accounts.models import User, Children
from .v2.levelsdict import *


class JsonDataSerializer(serializers.Serializer):
    jsonToDb = serializers.JSONField()

    class Meta:
        fields = (
            'jsonToDb',
        )
    
    def validate_jsonToDb(self, value):
        if 'levels' in value and 'header' in value:
            return value
        else:
            raise serializers.ValidationError({'jsonToDb': 'Missing header or levels dict'})


class HeaderCreateSerializer(serializers.ModelSerializer):
    game_key = serializers.CharField(source='gamekey')
    game_time = serializers.IntegerField(source='gametime')
    passed_levels = serializers.IntegerField(source='passedlevels')
    repeated_levels = serializers.IntegerField(source='repeatedlevels')
    played_levels = serializers.IntegerField(source='playedlevels')
    parent_id = serializers.PrimaryKeyRelatedField(
        source='parent',
        required=True,
        queryset=User.objects.all()
    )
    kid_id = serializers.PrimaryKeyRelatedField(
        source='cid',
        required=True,
        queryset=Children.objects.all()
    )

    class Meta:
        model = Header
        fields = (
            'id',
            'date',
            'parent_id',
            'kid_id',
            'game_key',
            'game_time',
            'passed_levels',
            'repeated_levels',
            'played_levels',
            'device',
            'version',
        )


class AssesmentSerializer(serializers.ModelSerializer):
    header = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Header.objects.all()
    )

    class Meta:
        model = Prueba
        fields = '__all__'
    
    def to_representation(self, obj):
        return dict(code='200')


class ArbolMusicalSerializer(serializers.ModelSerializer):
    header = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Header.objects.all()
    )

    class Meta:
        model = ArbolMusicalV2
        fields = '__all__'
        extra_kwargs = ArbolMusicalDict


    def to_representation(self, obj):
        return dict(code='200')


class ArenaMagicaSerializer(serializers.ModelSerializer):
    header = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Header.objects.all()
    )

    class Meta:
        model = ArenaMagicaV2
        fields = '__all__'
        extra_kwargs = ArenaMagicaDict
    
    def to_representation(self, obj):
        return dict(code='200')



class DondeQuedoLaBolitaSerializer(serializers.ModelSerializer):
    header = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Header.objects.all()
    )

    class Meta:
        model = DondeQuedoLaBolitaV2
        fields = '__all__'
        extra_kwargs = MonosDict
    
    def to_representation(self, obj):
        return dict(code='200')


class RioSerializer(serializers.ModelSerializer):
    header = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Header.objects.all()
    )

    class Meta:
        model = RioV2
        fields = '__all__'
        extra_kwargs = RioDict
    
    def to_representation(self, obj):
        return dict(code='200')



class JuegoDeSombrasSerializer(serializers.ModelSerializer):
    header = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Header.objects.all()
    )

    class Meta:
        model = SombrasV2
        fields = '__all__'
        extra_kwargs = SombrasDict
    
    def to_representation(self, obj):
        return dict(code='200')



class TesoroSerializer(serializers.ModelSerializer):
    header = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Header.objects.all()
    )

    class Meta:
        model = RecoleccionTesoroV2
        fields = '__all__'
        extra_kwargs = TesoroDict
    
    def to_representation(self, obj):
        return dict(code='200')
