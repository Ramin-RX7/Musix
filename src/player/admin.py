from django.contrib import admin

from .models import *

admin.site.register(Genre)
admin.site.register(Artist)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["title", "code"]
