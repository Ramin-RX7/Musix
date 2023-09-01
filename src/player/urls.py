from django.urls import path

from .views import SongView



app_name = "player"


urlpatterns = [
    path("song/<slug:code>", SongView.as_view(), name="song"),
]
