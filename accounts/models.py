from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phoneno, password=None, **extra_fields):
        """Create and save a User with the given email and password."""

        user = self.model(phoneno=phoneno, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        print("in final")
        return user

    def create_user(self, phoneno, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        print("in create user")
        return self._create_user(phoneno, password, **extra_fields)

    def create_superuser(self, phoneno, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        print("in superuser")
        return self._create_user(phoneno, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    REQUIRED_FIELDS = []
    phoneno = models.CharField(verbose_name='contact number',
                               max_length=12,
                               unique=True)
    USERNAME_FIELD = 'phoneno'

    objects = CustomUserManager()
