from django.db import models

# Create your models here.
class Tertiary_center(models.Model):
    name = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)

    def __str__(self):
        return self.name