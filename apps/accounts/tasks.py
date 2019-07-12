from reusable.sendgrid import EmailSendgrid
from celery import shared_task


@shared_task
def email_suscription_expire(sus_id):
    pass