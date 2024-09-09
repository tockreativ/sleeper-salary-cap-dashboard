from django import forms
from .models import Player, Team

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'team', 'position', 'fantasy_points']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'players']
