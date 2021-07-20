# STDLIB IMPORTS
import datetime

# DJANGO IMPORTS
from django.db import models
from django.utils import timezone
from datetime import timedelta

# APPLICATION IMPORTS
from reusable.constants import BLANK, REQUIRED, BLANK_NOT_NULL
from accounts.models import User, Children
from .managers import SuscriptionManager
from .helpers import get_finished_date
from reusable.tasks import send_email

TYPES_SUS_CHOICES = (
    ('unsuscribe', 'Sin subscripción'),
    ('monthly', 'Mensual'),
    ('quarterly', 'Trimestral'),
    ('monthly_inApp', 'Mensual comprada desde la App'),
    ('quarterly_inApp', 'Trimestral comprada desde la App')
)


class SuscriptionType(models.Model):
    price = models.IntegerField(**REQUIRED)
    name = models.CharField(
        choices=TYPES_SUS_CHOICES,
        max_length=50,
        default='unsuscribe'
    )
    description = models.TextField(**BLANK_NOT_NULL)

    class Meta:
        verbose_name = 'Tipo suscripcion'
        verbose_name_plural = 'Tipo de suscripciones'

    def __str__(self):
        return self.name

    def has_promo(self, code=None):
        promos = self.promos.filter(
            promo_code=code
        )
        if promos.exists():
            return promos.first()
        else:
            return None


class Promos(models.Model):
    amount = models.FloatField(**REQUIRED)
    description = models.TextField(**BLANK_NOT_NULL)
    unique = models.BooleanField(default=False)
    promo_code = models.CharField(max_length=200, **REQUIRED)
    suscription = models.ForeignKey(
        SuscriptionType,
        related_name='promos',
        **REQUIRED
    )

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'

    def __str__(self):
        return str(self.amount)


class Suscription(models.Model):
    user = models.ForeignKey(
        User,
        related_name='suscriptions',
        **BLANK
    )
    type = models.ForeignKey(
        SuscriptionType,
        related_name='suscriptions',
        **REQUIRED
    )
    children = models.OneToOneField(
        Children,
        related_name='suscription',
        on_delete=models.SET_NULL,
        **BLANK
    )
    start_date = models.DateTimeField(verbose_name='Fecha de inicio')
    finished_date = models.DateTimeField(verbose_name='Fecha fin')
    is_recurrent = models.BooleanField(default=False)
    trial = models.BooleanField(default=False)
    order = models.CharField(max_length=200, **BLANK)

    objects = SuscriptionManager()

    class Meta:
        verbose_name = 'Suscription'

    def update(self, *args, **kwargs):
        self.start_date = timezone.now()
        if 'finished_date' in kwargs:
            self.finished_date = kwargs['finished_date']
        else:
            self.finished_date = get_finished_date(self.type.name)
        self.save()

    def active(self):
        if self.trial is True:
            return False
        elif self.finished_date < timezone.now():
            return False
        else:
            return True

    def add_children(self, child):
        if not isinstance(child, Children):
            child = Children.objects.get(pk=child)
        self.children = child
        self.save()
        try:
            pass
            # email_context = {
            #     'name': self.user.display_name,
            #     'children_name': self.children.get_full_name,
            #     'date': self.finished_date.strftime('%d-%m-%Y'),
            #     'email': self.user.email
            # }
            # send_email.apply_async(
            #     ('compra_vencimiento', email_context),
            #     eta=timezone.now() - timedelta(days=5)
            # )
        except Exception as e:
            pass

    def remove_children(self):
        self.children = None
        self.delete()

    def can_view_test(self):
        if (self.type.name == 'quarterly' or self.type.name == 'quarterly_inApp') and self.active():
            return True
        else:
            return False

    @classmethod
    def create_trial(cls, user, children=None):
        instance = cls.objects.create(
            user=user,
            children=children,
            start_date=timezone.now(),
            finished_date=timezone.now() + timedelta(days=2),
            trial=True,
            type=SuscriptionType.objects.get(name='unsuscribe')
        )
        return instance

    @classmethod
    def create_new(cls, user, type, ids=[], number_of_suscriptions=1, **kwargs):  # NOQA
        for _ in range(int(number_of_suscriptions)):
            if len(ids) > 0:
                cid_id = ids.pop()
                children = user.childrens.get(pk=cid_id)
                if hasattr(children, 'suscription'):
                    children.suscription.remove_children()
                cls.objects.create(
                    user=user,
                    children=children,
                    type=SuscriptionType.objects.get(name=type),
                    start_date=timezone.now(),
                    finished_date=get_finished_date(type),
                    **kwargs
                )
                try:
                    email_context = {
                        'name': self.user.display_name,
                        'children_name': self.children.get_full_name,
                        'date': self.finished_date.strftime('%d-%m-%Y'),
                        'email': self.user.email
                    }
                    # send_email.apply_async(
                    #     ('compra_vencimiento', email_context),
                    #     # eta=timezone.now() - timedelta(days=5)
                    # )
                except Exception as e:
                    pass
            else:
                cls.objects.create(
                    user=user,
                    type=SuscriptionType.objects.get(name=type),
                    start_date=timezone.now(),
                    finished_date=get_finished_date(type),
                    **kwargs
                )
        return


class Order(models.Model):
    price = models.FloatField(default=0.00, **REQUIRED)
    max_kids = models.IntegerField(**REQUIRED)
    amount = models.FloatField(default=0.00, **REQUIRED)
    recurrency = models.CharField(max_length=50, **REQUIRED)  # NOQA
    promo_code = models.CharField(max_length=200, **BLANK_NOT_NULL)
    user_id = models.IntegerField(**REQUIRED)
    user_email = models.CharField(max_length=100, **REQUIRED)
    created_date = models.DateTimeField(auto_now_add=True)
    open_pay_id = models.CharField(max_length=200, **BLANK)
    open_pay_order_id = models.CharField(max_length=200, **BLANK)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'


class VerificationCode(models.Model):
    code = models.CharField(max_length=300, **BLANK)

    class Meta:
        verbose_name = 'Codigo verificacion'
