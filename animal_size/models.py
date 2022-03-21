from django.db import models

class AnimalSize(models.Model):
    name = models.CharField(max_length=7, null=False, blank=False, unique=True)
    description = models.CharField(max_length=250, null=False, blank=False)

    class Meta:
        db_table = 'animal_size'

    def __str__(self):
        return self.name