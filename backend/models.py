from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    fantasy_points = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name='teams')  # Add related_name

    def __str__(self):
        return self.name
