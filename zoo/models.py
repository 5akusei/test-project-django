from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from animal_size.models import AnimalSize

class Animal(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=6, blank=False, null=False)
    size = models.ForeignKey(AnimalSize, to_field='name', on_delete=models.SET_NULL, null=True, blank=True)
    life_span = models.PositiveIntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(150)])
    type_of_bird = models.CharField(max_length=80, blank=False, null=False)
    family = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'animal'