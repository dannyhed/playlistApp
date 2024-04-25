from django.db import models
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
#List of choices for major value in database, human readable name
    USER_TYPE = (
    ('L', 'Listener'),
    ('A', 'Artist')
    )
    is_active = False
    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    type = models.CharField(max_length=200, choices=USER_TYPE)
    #playlist = models.OneToOneField(Portfolio, null=True, on_delete=models.CASCADE, default=None, unique=True)
    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name


    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('playlist-detail', args=[str(self.id)])


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200) #eventually will be artist profile
    #add mp3 file or link
    playlist = models.ForeignKey(Playlist, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('song-detail', args=[str(self.id)])