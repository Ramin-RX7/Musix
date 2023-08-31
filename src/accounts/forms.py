from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ["email", "username", "password1", "password2"]
        model = User