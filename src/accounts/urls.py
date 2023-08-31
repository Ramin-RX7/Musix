from django.urls import path

from .views import Signup,Profile



app_name = "accounts"


urlpatterns = [
    path("signup/", Signup.as_view(), name="signup"),
    path("profile/", Profile, name="profile"),
]