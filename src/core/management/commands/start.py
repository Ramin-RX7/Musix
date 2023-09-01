from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from accounts.models import User
from player.models import Song,Artist,Genre


class Command(BaseCommand):
    help = 'Create required configs/models before first run'

    def handle(self, *args, **options):
        import os,shutil
        os.remove("./db.sqlite3")
        shutil.rmtree("./player/migrations/")
        shutil.rmtree("./accounts/migrations/")
        try:
            os.system("python manage.py makemigrations player")
            os.system("python manage.py makemigrations accounts")
            os.system("python manage.py migrate")
            user = User(username="admin", email="admin@admin.admin", is_superuser=True, is_staff=True)
            user.set_password("admin")
            user.save()
        except IntegrityError:
            pass

        artist = Artist.objects.create(name="MyArt")
        genre = Genre.objects.create(name="EDM")
        song = Song(title="ST",genre=genre,)
        song.save()
        song.artists.add(artist.pk)
        song.save()