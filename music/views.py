from django.shortcuts import render, get_object_or_404, redirect
from . models import Album, Song
from .forms import AlbumForm, SongForm
from django.views.generic import UpdateView


# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def create_album(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.album_cover = request.FILES['album_cover']
        album.save()
        return render(request, 'music/detail.html', {'album': album})
    return render(request, 'music/create_album.html', {'form': form})


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['album_name', 'artist_name', 'album_genre', 'album_cover']
    template_name = 'music/create_album.html'


def album_delete(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect('/')


def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        song = form.save(commit=False)
        song.album = album
        song.song_audio = request.FILES['song_audio']
        song.save()
        context = {
            'album': album,
            'message': 'Song Created Successfully!'
        }
        return render(request, 'music/detail.html', context)
    return render(request, 'music/create_song.html', {'form': form})


class SongUpdateView(UpdateView):
    model = Song
    fields = ['song_name', 'song_audio']
    template_name = 'music/create_song.html'


def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = get_object_or_404(Song, pk=song_id)
    song.delete()
    context = {
        'album': album,
        'message': 'Song Deleted Successfully!'
    }
    return render(request, 'music/detail.html', context)











