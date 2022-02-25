"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, event
from levelupapi.models.event_gamer import EventGamer


class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
        

    def list(self, request):
       
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.description=request.data["description"],
        event.date=request.data["date"],
        event.time=request.data["time"],
        event.organizer=request.data["organizer"],
        
        event_gamer = EventGamer.objects.get(pk=request.data["event_gamer"])

        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        
        
class EventSerializer(serializers.ModelSerializer):
    """JSON serializer 
    """
    class Meta:
        model = Event
        fields = ('id','description', 'date', 'time', 'organizer', 'game','attendees')