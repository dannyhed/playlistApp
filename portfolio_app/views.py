from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Playlist, Profile, Song
from .forms import ProjectForm, PlaylistForm
from . import spotify

# Create your views here.
def index(request):
   try:
      code = request.GET['code']
   except:
      return render(request, 'portfolio_app/index.html', {'playlists': Playlist.objects.all()})
   print("GOT CODE")
   return render(request, 'portfolio_app/index.html', {'playlists': Playlist.objects.all()})#, {'spotifyplaylists': spotify.getPlaylists(code)})
# Render the HTML template index.html with the data in the context variable.

def login(request):
   return redirect(spotify.authorization())

def playlist(request, args):
   return render(request, 'portfolio_app/playlist.html', {'playlist':Playlist.objects.get(id=args), 'songs': Song.objects.filter(playlist=Playlist.objects.get(id=args))})

def song(request, args):
   return render(request, 'portfolio_app/song.html', {'song':Song.objects.get(id=args)})#, 'Playlist':Song.objects.get(id=args).Playlist})

def profiles(request):
   return render(request, 'portfolio_app/profiles.html')#, {'Profiles': Profile.objects.all()})

def profileDetail(request, args):
   return render(request, 'portfolio_app/profile_detail.html')#, {'Profile':Profile.objects.get(id=args), 'id':args})

def newSong(request, args):
   if (request.method=="POST"):
      form = ProjectForm(request.POST)
      if (form.is_valid()):
         Song = form.save()
         return redirect('song-detail', Song.id)
   else:
      form = ProjectForm()
   return render(request, 'portfolio_app/new_song.html', {'Playlist':Playlist.objects.get(id=args), 'form':form, 'args':args})

def newPlaylist(request):
   if (request.method=="POST"):
      form = PlaylistForm(request.POST)
      if (form.is_valid()):
         Playlist = form.save()
         return redirect('playlist-detail', Playlist.id)
   else:
      form = PlaylistForm()
   return render(request, 'portfolio_app/new_playlist.html', {'form':form})

def delPlaylist(request, id):
   playlist=Playlist.objects.get(id=id)
   if (request.method=="POST"):
      playlist.delete()
      return redirect('/')
   return render(request, 'portfolio_app/del_playlist.html')

def editSong(request, args, id):
   song=Song.objects.get(id=id)
   if (request.method == 'POST'):
        form = ProjectForm(request.POST , instance=song)
        if (form.is_valid()):
            song = form.save()
            return redirect('playlist-detail', song.playlist.id)
   else:
        form = ProjectForm(instance=song)
   return render(request, 'portfolio_app/edit_song.html', {'playlist':Playlist.objects.get(id=args), 'form':form, 'args':args})

def delSong(request, args, id):
   song=Song.objects.get(id=id)
   if (request.method == 'POST'):
      song.delete()
      return redirect('playlist-detail', song.playlist.id)
   return render(request, 'portfolio_app/del_song.html', {'playlist':Playlist.objects.get(id=args), 'args':args, 'Song':song})
   
def editPlaylist(request, id):
   playlist=Playlist.objects.get(id=id)
   if (request.method == 'POST'):
      form = PlaylistForm(request.POST, instance=playlist)
      if (form.is_valid()):
         playlist = form.save()
         return redirect('playlist-detail', playlist.id)
   else:
      form = PlaylistForm(instance = playlist)
   return render(request, 'portfolio_app/edit_playlist.html', {'args':id, 'Playlist':playlist, 'form':form})