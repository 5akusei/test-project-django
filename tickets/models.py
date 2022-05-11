from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    description = models.CharField(max_length=250, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    img_url = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ticket_types'