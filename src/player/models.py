from datetime import datetime
from django.db import models

from core.models import BaseModel,CodeBased
from accounts.models import User




class Genre(BaseModel):
    name = models.CharField(max_length=25, unique=True)
    # parent_genre = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)



class Artist(BaseModel,CodeBased):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/artists/", null=True)



class Song(BaseModel,CodeBased):
    title = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    published_at = models.DateTimeField(default=datetime.now)
    cover = models.ImageField(upload_to="covers/song/", null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL,null=True)
    # audio_file = models.FileField(upload_to="songs/")



class Playlist(BaseModel,CodeBased):
    songs = models.ManyToManyField(Song)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)



class Like(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
