# STDLIB IMPORTS
from datetime import timedelta

# DJANGO CORE IMPORTS
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
# THIRD PARTY IMPORTS
from rest_framework import serializers

# TOWI IMPORTS
from ..models import Children, User, LinkedAccountsChildrens
from levels.models import ChildrenTowiIsland




class LoginSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    access = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()
    userExists = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    suscriptionsAvailables = serializers.SerializerMethodField()

    class Meta(object):
        fields = [
            'id', 'access', 'key', 'userExists',
            'children', 'suscriptionsAvailables',
        ]

    def get_id(self, obj):
        return obj.id

    def get_access(self, obj):
        return True

    def get_key(self, obj):
        return obj.key

    def get_userExists(self, obj):
        return True

    def get_children(self, obj):
        my_children = obj.childrens.all()
        list_linked = obj.shared_linked_accounts.all()
        children = []
        for child in my_children:
            children.append(ChildrenLoginSerializer(child).data)
        for linked in list_linked:
            if LinkedAccountsChildrens.objects.filter(linked_account=linked).exists():
                lac = LinkedAccountsChildrens.objects.get(linked_account=linked)
                children.append(ChildrenLoginSerializer(lac.cid).data)
        # return ChildrenLoginSerializer(obj.childrens.all(), many=True).data
        return children

    def get_suscriptionsAvailables(self, obj):
        return obj.suscriptions.availables().count()


class ChildrenLoginSerializer(serializers.ModelSerializer):
    cid = serializers.IntegerField(source='id')
    name = serializers.CharField(source='first_name')
    lastname = serializers.CharField(source='last_name')
    age = serializers.SerializerMethodField()
    active = serializers.SerializerMethodField()
    trial = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()
    picture = serializers.SerializerMethodField()
    pruebaDate = serializers.SerializerMethodField()

    class Meta(object):
        model = Children
        fields = [
            'cid', 'name', 'lastname',
            'active', 'trial', 'key', 'picture',
            'age', 'pruebaDate'
        ]

    def get_active(self, obj):
        return obj.suscription.active()

    def get_trial(self, obj):
        return obj.suscription.trial

    def get_key(self, obj):
        return obj.user.key

    def get_picture(self, obj):
        return settings.BLOB_URL + obj.picture.name

    def get_age(self, obj):
        return obj.age

    def get_pruebaDate(self, obj):
        ti = obj.towiIndexChild.last()
        if ti:
            return ti.date.strftime('%Y-%m-%d')
        else:
            return ""


class ProfilesSerializer(serializers.ModelSerializer):
    avatarClothes = serializers.CharField(source='avatarclothes')
    ownedItems = serializers.CharField(source='owneditems')
    activeMissions = serializers.SerializerMethodField()
    activeDay = serializers.IntegerField(source='activeday')
    rioFirstTime = serializers.BooleanField(source='rio_first_time')
    tesoroFirstTime = serializers.BooleanField(source='tesoro_first_time')
    arbolFirstTime = serializers.BooleanField(source='arbol_first_time')
    arenaFirstTime = serializers.BooleanField(source='arena_first_time')
    sombrasFirstTime = serializers.BooleanField(source='sombras_first_time')
    bolitaFirstTime = serializers.BooleanField(source='bolita_first_time')
    age = serializers.SerializerMethodField()
    testAvailable = serializers.SerializerMethodField()
    active = serializers.SerializerMethodField()
    suscriptionType = serializers.SerializerMethodField()
    trial = serializers.BooleanField(source='cid.suscription.trial')
    name = serializers.CharField(source='cid.get_full_name')
    rioLevelSet = serializers.BooleanField(source='rio_level_set')
    tesoroLevelSet = serializers.BooleanField(source='tesoro_level_set')
    arbolLevelSet = serializers.BooleanField(source='arbol_level_set')
    arenaLevelSet = serializers.BooleanField(source='arena_level_set')
    arenaLevelSet2 = serializers.BooleanField(source='arena_level_set2')
    sombrasLevelSet = serializers.BooleanField(source='sombras_level_set')
    bolitaLevelSet = serializers.BooleanField(source='bolita_level_set')
    islandShoppingList = serializers.SerializerMethodField()

    class Meta(object):
        model = ChildrenTowiIsland
        fields = (
            'cid', 'kiwis', 'avatar', 'avatarClothes',
            'ownedItems', 'activeMissions', 'age',
            'activeDay', 'rioFirstTime', 'tesoroFirstTime',
            'arbolFirstTime', 'bolitaFirstTime',
            'sombrasFirstTime', 'arenaFirstTime', 'testAvailable',
            'active', 'trial', 'name', 'suscriptionType',
            'rioLevelSet',
            'tesoroLevelSet',
            'arbolLevelSet',
            'arenaLevelSet',
            'arenaLevelSet2',
            'sombrasLevelSet',
            'bolitaLevelSet',
            'islandShoppingList',
        )

    def get_active(self, obj):
        #return obj.cid.suscription.active()
        print("************+  entro en get active ", obj," fin par obj ********")
        if obj.has_suscription():
            print("true")
            return obj.cid.suscription.active()
        else:
            print("false")
            return 'No suscription'

    def get_activeMissions(self, obj):
        if obj.session_date:
            if obj.session_date == timezone.now().date():
                return []
            else:
                #print("object active missions: ", obj.activemissions)
                if obj.activemissions:
                    return obj.activemissions.split(', ')
                else:
                    return None
        else:
            return obj.activemissions.split(', ')

    def get_age(self, obj):
        return obj.cid.age

    def get_suscriptionType(self, obj):
        if obj.has_suscription():
            print("true")
            return obj.cid.suscription.type.name
        else:
            print("false")
            return 'No suscription type'

    def get_testAvailable(self, obj):
        header = obj.cid.headers.filter(gamekey='PruebaEcologica').last()
        if header:
            date = header.date + timedelta(days=30)
            if date > timezone.now():
                return False
            else:
                return True
        else:
            return True

    def get_islandShoppingList(self, obj):
        if obj.island_shopping_list:
            return map(int, obj.island_shopping_list.split(','))
        else:
            return []


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
