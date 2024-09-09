from django.contrib import admin
from .models import Player, Team

# Customize the admin interface for the Player model
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'position', 'fantasy_points')
    search_fields = ('first_name', 'last_name', 'team')

# Customize the admin interface for the Team model
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register models with the admin site
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
