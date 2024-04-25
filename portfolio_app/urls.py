from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
        
    path('admin/', admin.site.urls),
    #connect path to portfolio_app urls
    #path('', include('portfolio_app.urls')),
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    
    #path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('playlist/<args>/', views.playlist, name='playlist-detail'),

    path('song/<args>/', views.song, name='song-detail'),

    path('playlist/<args>/new_song/', views.newSong, name='new-song'),

    path('new_playlist/', views.newPlaylist, name='new-playlist'),

    path('playlist/<args>/edit_song/<id>', views.editSong, name='edit-song'),

    path('playlist/<args>/del_song/<id>', views.delSong, name='del-song'),

    path('profiles/', views.profiles, name='profiles'),

    path('profiles/<args>', views.profileDetail, name='profile-detail'),

    path('playlist/<id>/edit_playlist', views.editPlaylist, name='edit-playlist'),
    
    path('playlist/<id>/del_playlist', views.delPlaylist, name='del-playlist'),
]

