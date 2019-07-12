from django.core.management.base import BaseCommand, CommandError
from accounts.models import Children


class Command(BaseCommand):
    help = 'Corrige los grados de los niños'

    def handle(self, *args, **options):
        for e in Children.objects.all():
            if e.grade:
                grado = e.grade
                if '1' in grado:
                    e.grade = '1 primaria'
                if '2' in grado:
                    e.grade = '2 primaria'
                if '3' in grado:
                    e.grade = '3 primaria'
                if '4' in grado:
                    e.grade = '4 primaria'
                if '5' in grado:
                    e.grade = '5 primaria'
                if '6' in grado:
                    e.grade = '6 primaria'
                if 'k' in grado:
                    e.grade = 'Kinder'
                if 'Prep' in grado:
                    e.grade = 'Preprimaria'
                e.save()
        self.stdout.write("Grados terminados", ending='')
