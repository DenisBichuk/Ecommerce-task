from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email address')
    )
    username = None

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password',)
