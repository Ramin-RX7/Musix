import re

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager

from core.models import BaseModel



class UserManager(DjangoUserManager):
    def get_by_natural_key(self, username):
        if re.fullmatch(r"(\w+)@(\w{2,})\.(\w{2,})", username):
            return self.get(email=username)
        elif username:
            return self.get(username=username)
        raise SystemError


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    _usertype_fields = models.TextChoices("Type","Normal VIP")
    account_type = models.CharField(choices=_usertype_fields.choices, max_length=6,default="Normal")

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
