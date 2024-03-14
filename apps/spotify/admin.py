from django.contrib import admin

from apps.spotify.models import Song, SongPlaylist, User, UserProfile, Artist, Album, Genre, SongGenre, Playlist

admin.site.register([User, UserProfile, Artist, Album, Genre, Song, SongPlaylist, SongGenre, Playlist])


