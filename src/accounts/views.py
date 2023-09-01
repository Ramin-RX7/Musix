import re

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import FormView,RedirectView
from django.contrib.auth import (authenticate, login as django_login, logout as django_logout)
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View

from .forms import SignupForm,LoginForm
from .models import User



class Signup(FormView):
    form_class = SignupForm
    success_url = reverse_lazy("accounts:profile")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class Login(FormView):

    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy("accounts:profile")

    def dispatch(self, request, *args, **kwargs):
        if isinstance(request.user, User):
            return redirect("panel:dashboard")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)
        cd = form.cleaned_data
        login_option = cd["login_option"]

        if re.fullmatch(r"(\w+)@(\w{2,})\.(\w{2,})", login_option):
            login_option_type = "email"
        else:
            login_option_type = "username"
        print(login_option_type)

        if user:=authenticate(self.request, **{login_option_type:login_option, "password":cd["password"]}):
            # django_login(self.request, user)
            print("login")
            if not cd["remind_me"]:
                self.request.session.set_expiry(0)
            return self.form_valid(form)
        else:
            form.add_error(None, "Invalid credentials")
            return self.form_invalid(form)

        # Should id put this in the form_valid() ??
        """
        try:
            if re.fullmatch(r"(\w+)@(\w{2,})\.(\w{2,})", login_option):
                user = User.objects.get(email=login_option)
                login_option_type = "email"
            else:
                user = User.objects.get(username=login_option)
                login_option_type = "username"
        except User.DoesNotExist:
            form.add_error(None,"The user does not exist")
            return self.form_invalid(form)

        if user.check_password(cd["password"]):
            django_login(self.request, user, "accounts.auth.UserAuthBackend")
            print("loggin user in")
            return self.form_valid(form)
        else:
            form.add_error(None,"invalid password")
            return self.form_invalid(form)
        """



def Profile(request):
    return HttpResponse("XX")
