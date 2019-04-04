from django import forms
from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_name', 'artist_name', 'album_genre', 'album_cover']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_name', 'song_audio']

