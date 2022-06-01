from django.db import models
from zones.models import Zone

class TicketType(models.Model):
    name = models.CharField(max_length=30)
    img_url = models.FileField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ticket_types'

class ZoneTicketType(models.Model):
    id_ticket_type = models.ForeignKey(TicketType, on_delete=models.SET_NULL, null=True)
    id_zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'zone_ticket_types'

class Ticket(models.Model):
    id_ticket_type = models.ForeignKey(TicketType, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    entrance_value = models.FloatField()
    reserved_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        db_table = 'tickets'