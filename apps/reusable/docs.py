from drf_yasg import openapi
from rest_framework import serializers


userkey_param = openapi.Parameter('userKey', openapi.IN_QUERY, description="User suscription key", type=openapi.TYPE_STRING)
gamekey_param = openapi.Parameter('gameKey', openapi.IN_QUERY, description="Game key", type=openapi.TYPE_STRING)
date_param = openapi.Parameter('date', openapi.IN_QUERY, description="Date", type=openapi.TYPE_STRING)
cid_param = openapi.Parameter('cid', openapi.IN_QUERY, description="Children ID", type=openapi.TYPE_INTEGER)
email_param = openapi.Parameter('parent_email', openapi.IN_QUERY, description="user email", type=openapi.TYPE_STRING)
json_param = openapi.Parameter('jsonToDb', openapi.IN_QUERY, description="json to load", type=openapi.TYPE_STRING)


class ActiveAccountSerializer(serializers.Serializer):
    active = serializers.BooleanField()

    class Meta:
        fields = ['active', ]


class CodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()

    class Meta:
        fields = ['code', ]


class ChildrenLevelsSerializer(serializers.Serializer):
    code = serializers.CharField()
    arbolMusicalLevel = serializers.IntegerField()
    arbolMusicalSublevel = serializers.IntegerField()
    rioLevel = serializers.IntegerField()
    rioSublevel = serializers.IntegerField()
    arenaMagicaLevel = serializers.IntegerField()
    arenaMagicaSublevel = serializers.IntegerField()
    monkeyLevel = serializers.IntegerField()
    monkeySublevel = serializers.IntegerField()
    sombrasLevel = serializers.IntegerField()
    sombrasSublevel = serializers.IntegerField()
    tesoroLevel = serializers.IntegerField()
    tesoroSublevel = serializers.IntegerField()
    arbolToday = serializers.IntegerField()
    rioToday = serializers.IntegerField()
    arenaToday = serializers.IntegerField()
    monkeyToday = serializers.IntegerField()
    sombrasToday = serializers.IntegerField()
    tesoroToday = serializers.IntegerField()

    class Meta:
        fields = [
            'code',
            'arbolMusicalLevel',
            'arbolMusicalSublevel',
            'rioLevel',
            'rioSublevel',
            'arenaMagicaLevel',
            'arenaMagicaSublevel',
            'monkeyLevel',
            'monkeySublevel',
            'sombrasLevel',
            'sombrasSublevel',
            'tesoroLevel',
            'tesoroSublevel',
            'arbolToday',
            'rioToday',
            'arenaToday',
            'monkeyToday',
            'sombrasToday',
            'tesoroToday',
        ]
