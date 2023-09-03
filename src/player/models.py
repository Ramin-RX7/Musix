from datetime import datetime
from django.db import models

from core.models import BaseModel,CodeBased
from accounts.models import User




class Genre(BaseModel):
    name = models.CharField(max_length=25, unique=True)
    # parent_genre = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Artist(BaseModel,CodeBased):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True, default="")
    image = models.ImageField(upload_to="images/artists/", null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name



class Song(BaseModel,CodeBased):
    title = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    published_at = models.DateTimeField(default=datetime.now)
    cover = models.ImageField(upload_to="covers/song/", null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL,null=True)
    audio_file = models.FileField(upload_to="songs/", null=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def get_artists(self):
        return ", ".join(map(str,self.artists.all()))



class Playlist(BaseModel,CodeBased):
    name = models.CharField(max_length=25)
    songs = models.ManyToManyField(Song)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/playlists/", null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class Like(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
