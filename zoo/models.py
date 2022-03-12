from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Animal(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=6, blank=False, null=False)
    life_span = models.PositiveIntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(150)])
    type_of_bird = models.CharField(blank=False, null=False)
    family = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)