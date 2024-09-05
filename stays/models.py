from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Host model
class Host(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NON_BINARY = 'NB'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (NON_BINARY, "Non-Binary"),
        (OTHER, "Other")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=OTHER,
        null=True
    )
    rating = models.IntegerField(blank=True, null=True)
    superhost = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}'
    
# Stays model
class Stay(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    location = models.CharField(max_length=255)
    host = models.ForeignKey(Host, on_delete=models.PROTECT, related_name='host')
    guests = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    features = models.TextField(max_length=510)
    description = models.TextField(max_length=510)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title



