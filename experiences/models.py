from django.db import models

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    location = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    guests = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    features = models.TextField(max_length=510)
    description = models.TextField(max_length=510)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

