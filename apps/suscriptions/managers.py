# Core Django Imports
from django.db import models
from django.utils import timezone
from django.db.models import Q


class SuscriptionQuerySet(models.QuerySet):
    def active(self):
        return self.filter(
            finished_date__gte=timezone.now(),
            trial=False
        )

    def inactive(self):
        return self.filter(
            Q(finished_date__lte=timezone.now()) |
            Q(trial=True)
        )

    def availables(self):
        return self.filter(
            finished_date__gte=timezone.now(),
            children__isnull=True,
            trial=False
        ).exclude(
            type__name='unsuscribe'
        )


class SuscriptionManager(models.Manager):
    def get_queryset(self):
        return SuscriptionQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()

    def availables(self):
        return self.get_queryset().availables()
