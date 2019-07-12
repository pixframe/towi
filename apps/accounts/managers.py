# Stdlib IMPORTS
import string
import random
import hashlib

# DJANGO CORE IMPORTS
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.key = self._game_key_generator('{}{}'.format(user.id, user.email))
        user.vcode = self._create_vinculationCode(user.id)
        user.link_id = self._create_linkId(user.id)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def _create_vinculationCode(self, id):
        code = ''.join(
            random.choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(40)
        )
        return '{}'.format(id) + code

    def _create_linkId(self, id):
        code = ''.join(
            random.choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(5)
        )
        return 'PXL{}'.format(id) + code

    def _game_key_generator(self, string):
        return hashlib.sha256(string.encode()).hexdigest()


class ChildrenManager(models.Manager):
    def get_queryset(self):
        return super(ChildrenManager, self).get_queryset().filter(status='active')


class ResearchesManager(models.Manager):
    def get_queryset(self):
        return super(ResearchesManager, self).get_queryset().filter(
            user_type='investigador'
        )
