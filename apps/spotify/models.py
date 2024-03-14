from django.contrib.auth.models import AbstractUser
from django.db.models import Model, ForeignKey, CASCADE, DateTimeField, ImageField, CharField, DateField, \
    IntegerField, EmailField, ManyToManyField

from apps.spotify.utils import avatar_path


class Abstract(Model):
    created = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = ImageField(upload_to=avatar_path)

    def __str__(self):
        return self.username


class UserProfile(Model):
    email = EmailField(unique=True)
    user = ForeignKey(User, on_delete=CASCADE)
    gender = CharField(max_length=12)
    birthdate = DateField(null=True)
    country = CharField(max_length=30)

    def __str__(self):
        return self.user


class Artist(Model):
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    follower = IntegerField()

    def __str__(self):
        return self.first_name


class Album(Abstract):
    author = ForeignKey(Artist, on_delete=CASCADE)
    title = CharField(max_length=128)
    cover = ImageField(upload_to=avatar_path)

    def __str__(self):
        return self.title


class Song(Abstract):
    title = CharField(max_length=128)
    cover = ImageField(upload_to=avatar_path)
    album = ForeignKey(Album, on_delete=CASCADE, related_name='songs')

    def __str__(self):
        return self.title


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class SongGenre(Abstract):
    song_id = ManyToManyField(Song, related_name='genres')
    genre_id = ManyToManyField(Genre, related_name='songs')

    def __str__(self):
        return f"{self.song}-{self.genre}"


class Playlist(Model):
    title = CharField(max_length=128)
    owner = ForeignKey(User, on_delete=CASCADE, related_name='playlists')

    def __str__(self):
        return self.title


class SongPlaylist(Model):
    song_id = ManyToManyField(Song)
    playlist_id = ManyToManyField(Playlist, related_name='songs')

    def __str__(self):
        return f"{self.song_id}-{self.playlist_id}"

