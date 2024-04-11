from django.db import models

# Create your models here.
class Hospital_center(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    Town = models.CharField(max_length=100)
    Region = models.CharField(max_length=100)
    District = models.CharField(max_length=100)

    def __str__(self):
        return self.name