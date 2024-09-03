from django.db import models

# Create your models here.

class Stay(models.Model):
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


class host(models.Model):
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

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=OTHER,
    )
    rating = models.IntegerField()
    superhost = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}'

