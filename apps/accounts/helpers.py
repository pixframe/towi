# STDLIB IMPORTS
import string
import random

# DJANGO CORE IMPORTS
from django.utils import timezone

# THIRD APPS IMPORTS
from rest_framework_jwt.settings import api_settings

# TOWI IMPORTS
from .models import (
    LinkedAccounts,
    LinkedAccountsChildrens,
    Children,
    User
)


def deactivate_childrens(user_id):
    '''
        Method to deactivate childrens with expired suscription
    '''
    try:
        user = User.objects.get(pk=user_id)
        for child in user.childrens.all():
            child.suscription.active()
    except User.DoesNotExist:
        pass


################################
# #### FUNCIONES INVITACION  ###
################################


def get_shared_childs(user):
    '''
        Method that returns the shared childs
    '''
    accounts = LinkedAccountsChildrens.objects.filter(
        linked_account__in=user.shared_linked_accounts.all(),
        auth=True
    ).select_related('cid')
    return accounts


def get_sharing_childs(user):
    '''
        Method that returns the sharing childs
    '''
    accounts = LinkedAccountsChildrens.objects.filter(
        linked_account__in=user.owner_linked_accounts.all(),
        auth=True
    ).select_related('cid')
    return accounts


def pending_approval_invitiations(user):
    '''
        Method that returns the pending invitations
        from shared childrens
    '''
    pending_approval = LinkedAccountsChildrens.objects.filter(
        linked_account__in=user.shared_linked_accounts.all(),
        auth=False
    ).select_related('cid')
    return pending_approval


def pending_to_approve_invitiations(user):
    '''
        Funcion que regresa las invitaciones enviadas
        que estan pendientes de aprobacion por el otro
        usuario
    '''
    childrens = Children.objects.none()
    prending_to_approve = LinkedAccountsChildrens.objects.filter(
        linked_account__in=user.owner_linked_accounts.all(),
        auth=False
    ).select_related('cid')
    return prending_to_approve
