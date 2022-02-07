from turtle import title
from django.db import models

from levelupapi.models import game_type



class Game(models.Model):
    title = models.CharField(max_length=55)
    number_of_players = models.IntegerField()
    maker = models.CharField(max_length=55)
    skill_level = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    