from django.shortcuts import render, get_object_or_404
from . models import Album
from .forms import AlbumForm


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




