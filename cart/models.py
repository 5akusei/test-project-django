from django.db import models
from user.models import User
from tickets.models import TicketType

class Cart(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id_ticket_type = models.ForeignKey(TicketType, on_delete=models.SET_NULL, null=True)
    is_sold = models.BooleanField(default=False)
    quantity = models.IntegerField()
    entrance_value = models.FloatField()
    reserved_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carts'