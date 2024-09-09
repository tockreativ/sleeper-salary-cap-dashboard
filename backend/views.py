from django.shortcuts import render, get_object_or_404
from .models import Player, Team
from .forms import PlayerForm, TeamForm
from django.http import HttpResponseRedirect

# View for listing all players
def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', {'players': players})

# View for showing details of a specific player
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'player_detail.html', {'player': player})

# View for creating a new player
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/players/')
    else:
        form = PlayerForm()
    return render(request, 'create_player.html', {'form': form})

# View for listing all teams
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

# View for showing details of a specific team
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'team_detail.html', {'team': team})

# View for creating a new team
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams/')
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})
