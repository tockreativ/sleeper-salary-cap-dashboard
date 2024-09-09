from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.player_list, name='player_list'),          # List of all players
    path('players/<int:pk>/', views.player_detail, name='player_detail'),  # Detail view of a specific player
    path('teams/', views.team_list, name='team_list'),                # List of all teams
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),   # Detail view of a specific team
    path('players/add/', views.create_player, name='create_player'),  # Create new player
    path('teams/add/', views.create_team, name='create_team'),        # Create new team
]
