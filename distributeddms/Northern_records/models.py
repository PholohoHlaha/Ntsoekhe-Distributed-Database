from django.db import models

# Create your models here.
class PatientRecord(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    region = models.CharField(max_length=100)
    diagnosis = models.TextField()
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)

    # Additional fields as needed

    def __str__(self):
        return self.name
