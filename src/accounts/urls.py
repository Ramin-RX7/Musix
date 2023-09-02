from django.urls import path,re_path

from .views import *



app_name = "accounts"


urlpatterns = [
    path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    re_path(r"profile/(?P<username>\w*)", ProfileView.as_view(), name="profile"),
]