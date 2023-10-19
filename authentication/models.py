# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    #use email as a unique identifier 
    USERNAME_FIELD = 'email'

    #A list of field names that will be prompted for when creating a superuser via
    #createsuperuser management command.
    REQUIRED_FIELDS = ('username', )

    objects = CustomUserManager()

    def __str__(self):
        return self.email



