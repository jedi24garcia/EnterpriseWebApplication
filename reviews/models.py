from django.db import models
from django.contrib.auth.models import User
from stays.models import Stay

# Create your models here.
# Review model

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    property = models.ForeignKey(Stay, on_delete=models.PROTECT, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.property.title
