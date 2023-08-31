from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    _usertype_fields = models.TextChoices("Type","Normal VIP")
    user_type = models.CharField(choices=_usertype_fields.choices, max_length=6,default="Normal")
