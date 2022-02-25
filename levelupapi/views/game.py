"""View module for handling requests about game s"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game


class GameView(ViewSet):
    """Level up game s view"""

    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
        

    def list(self, request):
       
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["number_of_players"]
        game.skill_level = request.data["skill_level"]

        game_type = GameType.objects.get(pk=request.data["game_type"])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        
        
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game
    """
    class Meta:
        model = Game
        fields = ('id', 'title','number_of_players','maker','skill_level','gamer','game_type')