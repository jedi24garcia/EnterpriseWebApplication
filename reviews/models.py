from django.db import models
from django.contrib.auth.models import User
from stays.models import Stay
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# Review model

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    property = models.ForeignKey(Stay, on_delete=models.PROTECT, null=True)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    comments = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.property.title
