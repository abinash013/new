from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Album,Song
# Create your views here.

#music
def index(request):
    all_albums=Album.objects.all()
    context={
        'all_albums':all_albums
    }

    return render(request,'music/index.html',context)


#particular song
def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)

    return render(request,'music/detail.html',{'album':album})

def favourite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError):
        return render(request, 'music/detail.html' , {'album':album, 'error_message':"You didnt select valid song"})
    else:
        selected_song.is_favourite=not( selected_song.is_favourite)
        selected_song.save()
        return render(request, 'music/detail.html' ,{'album':album})