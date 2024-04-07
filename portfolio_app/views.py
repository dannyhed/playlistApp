from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Playlist, Profile, Song
from .forms import ProjectForm, PortfolioForm

# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render(request, 'portfolio_app/index.html')#, {'Playlists': Playlist.objects.all(), 'Songs': Song.objects.all(), 'Profiles': Profile.objects.all()})

def playlist(request, args):
   return render(request, 'portfolio_app/portfolio.html')#, {'Playlist':Playlist.objects.get(id=args), 'Songs': Song.objects.filter(Playlist=Playlist.objects.get(id=args))})

def song(request, args):
   return render(request, 'portfolio_app/project.html')#, {'Song':Song.objects.get(id=args), 'Playlist':Song.objects.get(id=args).Playlist})

def profiles(request):
   return render(request, 'portfolio_app/students.html')#, {'Profiles': Profile.objects.all()})

def profileDetail(request, args):
   return render(request, 'portfolio_app/student_detail.html')#, {'Profile':Profile.objects.get(id=args), 'id':args})

def newSong(request, args):
   if (request.method=="POST"):
      form = ProjectForm(request.POST)
      if (form.is_valid()):
         Song = form.save()
         return redirect('portfolio-detail', Song.Playlist.id)
   else:
      form = ProjectForm()
   return render(request, 'portfolio_app/new_project.html', {'Playlist':Playlist.objects.get(id=args), 'form':form, 'args':args})

def editSong(request, args, id):
   Song=Song.objects.get(id=id)
   if (request.method == 'POST'):
        form = ProjectForm(request.POST , instance=Song)
        if (form.is_valid()):
            Song = form.save()
            return redirect('portfolio-detail', Song.Playlist.id)
   else:
        form = ProjectForm(instance=Song)
   return render(request, 'portfolio_app/edit_project.html', {'Playlist':Playlist.objects.get(id=args), 'form':form, 'args':args})

def delSong(request, args, id):
   Song=Song.objects.get(id=id)
   if (request.method == 'POST'):
      Song.delete()
      return redirect('Playlist-detail', Song.Playlist.id)
   return render(request, 'portfolio_app/del_project.html', {'Playlist':Playlist.objects.get(id=args), 'args':args, 'Song':Song})
   
def editPlaylist(request, args):
   Playlist=Playlist.objects.get(id=args)
   if (request.method == 'POST'):
      form = PortfolioForm(request.POST, instance=portfolio)
      if (form.is_valid()):
         portfolio = form.save()
         return redirect('Playlist-detail', Playlist.id)
   else:
      form = PortfolioForm(instance = portfolio)
   return render(request, 'portfolio_app/edit_portfolio.html', {'args':args, 'Playlist':Playlist, 'form':form})