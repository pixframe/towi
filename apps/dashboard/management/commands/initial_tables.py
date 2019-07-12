from django.core.management.base import BaseCommand, CommandError
from suscriptions.models import SuscriptionType
from accounts.models import UserType


class Command(BaseCommand):
    help = 'Corrige los grados de los niños'

    def handle(self, *args, **options):
        SuscriptionType.objects.create(
            name='unsuscribe',
            price=0,
        )
        self.stdout.write("Tabla unsuscribed creada", ending='')

        SuscriptionType.objects.create(
            name='monthly',
            price=79,
        )
        self.stdout.write("Tabla monthly creada", ending='')

        SuscriptionType.objects.create(
            name='quarterly',
            price=199,
        )
        self.stdout.write("Tabla quarterly creada", ending='')

        SuscriptionType.objects.create(
            name='quarterly_inApp',
            price=199,
        )
        self.stdout.write("Tabla quarterly creada", ending='')

        SuscriptionType.objects.create(
            name='monthly_inApp',
            price=79,
        )
        self.stdout.write("Tabla quarterly creada", ending='')
