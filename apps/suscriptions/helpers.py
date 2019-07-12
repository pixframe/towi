# STDLIB IMPORTS
from datetime import timedelta
from django.utils import timezone


def get_finished_date(period='monthly'):
    if period in ['monthly', 'monthly_inApp']:
        return timezone.now() + timedelta(days=30)
    elif period in ['quarterly', 'quarterly_inApp']:
        return timezone.now() + timedelta(days=90)
    else:
        return timezone.now()
