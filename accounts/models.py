from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email address is required')

        if not name:
            raise ValueError('Your name is required')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=60, unique=True)
    name = models.CharField(blank=False, null=False, max_length=20)
    isStaff = models.BooleanField(blank=False, null=False, default=False)
    isAdmin = models.BooleanField(blank=False, null=False, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()
