from time import time
from django.db import models

from levelupapi.models import event_gamer



class Event(models.Model):
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")
    
def create(self, request):
    """Handle POST operations

    Returns
        Response -- JSON serialized game instance
    """
    
    event_gamer = EventGamer.objects.get(pk=request.data["event_gamer"])

    event = Event.objects.create(
        description=request.data["description"],
        date=request.data["date"],
        time=request.data["time"],
        organizer=request.data["organizer"],
        gamer=request.data["gamer"],
        event_gamer=event_gamer,
        
    )
    serializer = EventSerializer(event)
    return Response(serializer.data)