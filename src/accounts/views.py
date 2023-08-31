from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SignupForm



class Signup(FormView):
    form_class = SignupForm
    success_url = reverse_lazy("accounts:profile")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def Profile(request):
    return HttpResponse("XX")
