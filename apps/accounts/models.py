# STDLIB IMPORTS
import datetime
from datetime import date

# DJANGO IMPORTS
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

# APPLICATION IMPORTS
from .managers import UserManager, ChildrenManager
from .choices import *
from reusable.constants import BLANK, REQUIRED, BLANK_NOT_NULL


class UserType(models.Model):  # NO SE USA MAS
    description = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Tipo usuario'

    def __str__(self):
        return self.description


class Center(models.Model):
    name = models.CharField(max_length=300, **REQUIRED)
    picture = models.ImageField(upload_to='center', **BLANK)

    class Meta:
        verbose_name = 'Centro'

    def __str__(self):
        return self.name.title()


class School(models.Model):
    name = models.CharField(max_length=200, **REQUIRED)
    type = models.CharField(
        max_length=50,
        choices=SCHOOL_TYPE_CHOICES,
        **BLANK_NOT_NULL
    )
    regular_special = models.CharField(
        max_length=100,
        choices=REGULAR_SPECIAL_CHOICES,
        **BLANK_NOT_NULL
    )
    mixed_differetiated = models.CharField(
        max_length=100,
        choices=MIXED_CHOICES,
        **BLANK_NOT_NULL
    )
    city = models.CharField(max_length=300, **BLANK_NOT_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Escuela'


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    # Required fields
    email = models.EmailField(max_length=100, unique=True, **BLANK_NOT_NULL)
    password = models.CharField(max_length=100, **REQUIRED)

    # Personal info
    first_name = models.CharField(max_length=100, **BLANK_NOT_NULL)
    last_name = models.CharField(max_length=100, **BLANK_NOT_NULL)
    school = models.ForeignKey(School, related_name='users', **BLANK)
    country = models.CharField(max_length=100, **BLANK_NOT_NULL)
    state = models.CharField(max_length=100, **BLANK_NOT_NULL)
    genre = models.CharField(max_length=20, choices=GENDER_CHOICES, **BLANK_NOT_NULL)  # NOQA
    relation = models.CharField(max_length=100, **BLANK_NOT_NULL)
    picture = models.ImageField(
        upload_to='avatars',
        default='/avatars/default_user.png',
        **BLANK_NOT_NULL
    )
    dob = models.DateField(**BLANK)
    fb_id = models.CharField(max_length=200, **BLANK_NOT_NULL)
    phone = models.CharField(max_length=15, **BLANK)
    specialty = models.CharField(max_length=100, **BLANK_NOT_NULL)  # NOQA
    greeting = models.CharField(max_length=100, **BLANK_NOT_NULL)
    center = models.OneToOneField(Center, **BLANK)
    confirmed_email = models.BooleanField(default=False)

    # Vinculation fields
    # codigo random VERIFICAR EL CORREO UNICAMENTE 40 caracteres
    vcode = models.CharField(max_length=500)
    # PXLCODIGO RANDOM CON ESTE SE VINCULA 5 digitos despues de pxl
    link_id = models.CharField(max_length=15)

    # System info fields
    user_type = models.CharField(max_length=50, choices=SPECIALITY_CHOICES, default='familiar')  # NOQA
    researcher = models.BooleanField(default=False)  # Es investigador?
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')  # NOQA
    key = models.CharField(max_length=240, **BLANK)
    openpay_token = models.CharField(max_length=200, **BLANK)
    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    is_staff = models.BooleanField(default=True, verbose_name='Es staff')

    # Por borrar
    register_date = models.DateTimeField(
        default=timezone.now,
        **BLANK_NOT_NULL
    )
    account_type = models.IntegerField(**BLANK)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name).title()

    @property
    def get_short_name(self):
        return self.first_name.title()

    @property
    def display_name(self):
        if self.first_name:
            return self.first_name.title()
        else:
            return self.email

    @property
    def key_string(self):
        return '{}{}'.format(self.id, self.email)

    def get_inactive_childrens(self):
        return self.childrens.filter(
            id__in=self.suscriptions.inactive().values('children_id')
        )

    def get_active_childrens(self):
        return self.childrens.filter(
            id__in=self.suscriptions.active().values('children_id')
        )

    def available_kids(self):
        return self.suscriptions.availables()

    def suscription_ends(self, period='month'):
        if period in ['month', 'year']:
            if period == 'month':
                date = datetime.datetime.now().strftime("%Y-%m")
                return self.suscriptions.filter(
                    finished_date__startswith=date
                ).exclude(
                    trial=True
                )
            if period == 'year':
                return self.suscriptions.filter(
                    finished_date__month=timezone.now().year
                )
        else:
            return

    def create_children(self, first_name, dob, **kwargs):
        children = Children.objects.create(
            user=self,
            first_name=first_name,
            dob=dob,
            **kwargs
        )
        return children

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email


class Children(models.Model):
    objects = ChildrenManager()
    user = models.ForeignKey(User, related_name='childrens', **REQUIRED)  # NOQA
    first_name = models.CharField(max_length=100, **REQUIRED)
    last_name = models.CharField(max_length=100, **BLANK_NOT_NULL)
    dob = models.DateField(**BLANK)
    laterality = models.CharField(
        max_length=100,
        choices=LATERALITY_CHOICES,
        default='desconocido'
    )
    videogames_usage = models.FloatField(**BLANK)
    learning_disabilities = models.CharField(max_length=300, **BLANK_NOT_NULL)
    failed_grades = models.IntegerField(**BLANK)  # CAMBIAR A ENTEROS
    school = models.ForeignKey(School, **BLANK)
    grade = models.CharField(
        max_length=100,
        choices=SCHOOLARSHIP_CHOICES,
        **BLANK_NOT_NULL
    )
    genre = models.CharField(
        max_length=100,
        choices=GENDER_CHOICES,
        **BLANK_NOT_NULL
    )
    school_name = models.CharField(max_length=100, **BLANK_NOT_NULL)
    email = models.CharField(max_length=100, **BLANK_NOT_NULL)
    picture = models.ImageField(
        upload_to='avatars',
        default='/avatars/default_user.png',
        **BLANK_NOT_NULL
    )
    register_date = models.DateTimeField(auto_now_add=True)
    diagnostic = models.TextField(**BLANK)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='active'
    )

    class Meta:
        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'

    def __str__(self):
        return self.get_full_name

    @property
    def apellido_paterno(self):
        if self.lastname:
            return self.last_name.split(' ')[0]
        else:
            return ""

    @property
    def apellido_materno(self):
        if self.lastname:
            try:
                return self.last_name.split(' ')[1]
            except Exception:
                return ""
        else:
            return ""

    @property
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).title()

    @property
    def age(self):
        if self.dob:
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        else:
            return None

    @property
    def is_active(self):
        return self.suscription.active()

    def total_sessions(self, gamekey=None):
        return self.headers.filter(gamekey=gamekey).count()

    def total_time(self, gamekey):
        return self.headers.filter(
            gamekey=gamekey
        ).values(
            'gametime'
        ).aggregate(
            Count('gametime')
        )

    def played_levels(self, gamekey):
        return self.headers.filter(
            gamekey=gamekey
        ).values(
            'playedlevels'
        ).aggregate(
            Count('playedlevels')
        )

    def passed_levels(self, gamekey):
        return self.headers.filter(
            gamekey=gamekey
        ).values(
            'passedlevels'
        ).aggregate(
            Count('passedlevels')
        )

    def last_session_date(self, gamekey):
        session = self.headers.filter(gamekey=gamekey).last()
        return session.date

    def game_frequency(self, gamekey):
        date = timezone.now().date()
        monday2 = date - timedelta(days=date.weekday())
        header = self.headers.filter(
            gamekey=gamekey,
        ).first()
        if header:
            monday1 = (header.date.date() - timedelta(days=header.date.date().weekday()))  # NOQA
            weeks = (monday2 - monday1).days / 7
            result = self.headers.filter(
                gamekey=gamekey,
            ).count() / weeks
            return result
        else:
            return 0

    def totalcorrect_percentage(self, gamekey):
        return self.headers.filter(
            gamekey=gamekey
        ).aggregate(
            Avg('gametime')
        )

    def totalerrors_average(self, gamekey):
        pass


class Group(models.Model):
    user = models.ForeignKey(User, null=True, blank=False)
    name = models.CharField(null=False, blank=False, max_length=100)
    children = models.ManyToManyField(Children, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name).title()


class LinkedAccounts(models.Model):
    '''
        TABLA PARA CREAR UN LINK ENTRE DOS PERSONAS
        Y PUEDAN COMPARTIRSE NIÑOS
    '''
    owner_user = models.ForeignKey(
        User,
        related_name='owner_linked_accounts',
        **REQUIRED
    )
    shared_user = models.ForeignKey(
        User,
        related_name='shared_linked_accounts',
        **REQUIRED
    )

    def __str__(self):
        return '{} comparte a {}'.format(self.owner_user, self.shared_user)

    class Meta:
        verbose_name_plural = 'Usuarios Vinculados'
        unique_together = ('owner_user', 'shared_user')


class LinkedAccountsChildrens(models.Model):
    '''
        ES LA TABLA PARA VINCULAR AL NIÑO CON UNA AUTORIZACION(linkedaccounts)
        UNO A MUCHOS NIÑOS
        EL CAMPO AUTH ES PARA Desvincular A UN NIÑO
    '''
    linked_account = models.ForeignKey(
        LinkedAccounts,
        related_name='childrens'
    )
    cid = models.ForeignKey(
        Children,
        related_name='linked_accounts'
    )
    auth = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.linked_account, self.cid)

    class Meta:
        verbose_name_plural = 'Option de Cuentas Ligadas'
        unique_together = ('linked_account', 'cid')


class FreeTrial(models.Model):
    md5_device = models.CharField(max_length=100)
    trial_id = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Free Trial'
