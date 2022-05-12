from django.db import models
from zones.models import Zone

class Ticket(models.Model):
    name = models.CharField(max_length=30)
    zones = models.ManyToManyField(Zone, through='ZoneTickets')

    class Meta:
        db_table = 'tickets'

class ZoneTickets(models.Model):
    available_zones = models.ForeignKey(Zone, on_delete=models.SET_DEFAULT, default='')
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_DEFAULT, default='')
    value = models.FloatField()
    reserved_date = models.DateTimeField()
    generated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'zone_tickets'