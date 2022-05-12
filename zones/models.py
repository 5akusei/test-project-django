from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Zone(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    value = models.FloatField()
    img_url = models.FileField(max_length=255)
    max_capacity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'zones'