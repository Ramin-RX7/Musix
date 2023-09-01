from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User



class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ["email", "username", "password1", "password2"]
        model = User



class LoginForm(forms.Form):
    login_option = forms.CharField(max_length=25)
    password = forms.CharField(
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': "Password..."
        })
    )
    remidn_me = forms.BooleanField(initial=True)
