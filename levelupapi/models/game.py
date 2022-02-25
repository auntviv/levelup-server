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
    
    
def create(self, request):
    """Handle POST operations

    Returns
        Response -- JSON serialized game instance
    """
    gamer = Gamer.objects.get(user=request.auth.user)
    game_type = GameType.objects.get(pk=request.data["game_type"])

    game = Game.objects.create(
        title=request.data["title"],
        maker=request.data["maker"],
        number_of_players=request.data["number_of_players"],
        skill_level=request.data["skill_level"],
        gamer=gamer,
        game_type=game_type
    )
    serializer = GameSerializer(game)
    return Response(serializer.data)