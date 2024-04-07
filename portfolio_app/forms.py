from django.forms import ModelForm
from .models import Song, Playlist

class ProjectForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

class PortfolioForm(ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'
