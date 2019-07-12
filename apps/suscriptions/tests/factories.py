import factory
from datetime import timedelta

from django.utils import timezone

from ..models import Suscription, SuscriptionType
from accounts.tests.factories import UserFactory, ChildrenFactory


class SuscriptionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Suscription

    user = factory.SubFactory(UserFactory())
    children = factory.SubFactory(ChildrenFactory)
    start_date = factory.Faker('date_time')
    finished_date = factory.Faker('date_time')
    type = factory.Iterator(SuscriptionType.objects.all())
