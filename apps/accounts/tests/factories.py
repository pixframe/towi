import factory

from django.utils import timezone

from accounts.models import User, Children


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    email = factory.Faker('safe_email')
    password = factory.Faker('password')
    key = 'adsufasjdbfasdlkfabjsdkf'


class ChildrenFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Children
    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    dob = factory.Faker('date_time')
