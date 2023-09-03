from django.urls import path

from .views import SongView,PlaylistView,LikeView,PlaylistListView



app_name = "player"


urlpatterns = [
    path("song/<slug:code>/", SongView.as_view(), name="song"),
    path("playlist/<slug:code>/", PlaylistView.as_view(), name="playlist"),
    path("like/", LikeView.as_view(), name="like"),
    path("playlists/", PlaylistListView.as_view(), name="playlists"),
]
