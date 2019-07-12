from .sendgrid import EmailSendgrid
from celery import shared_task
from accounts.helpers import deactivate_childrens
from levels.helpers import session_changer


@shared_task
def send_email(template, context):
    EmailSendgrid(template, context)


@shared_task
def deactivate_childs(user):
    deactivate_childrens(user)

@shared_task
def email_childrens_to_expire(user):
    email_childrens_to_expire(user)


@shared_task
def cti_session_change(cti_id):
    session_changer(cti_id)
