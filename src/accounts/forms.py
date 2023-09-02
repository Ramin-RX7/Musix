from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User



class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ["email", "username", "password1", "password2"]
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["name"].widget.attrs.update({"class": "special"})
        for field_name,field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})


class LoginForm(forms.Form):
    login_option = forms.CharField(max_length=25)
    password = forms.CharField(
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': "Password..."
        })
    )
    remind_me = forms.BooleanField(required=False, initial=True)
