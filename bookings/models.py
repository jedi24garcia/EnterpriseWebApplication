from django.db import models
from django.contrib.auth.models import User
from stays.models import Stay

# Create your models here.
# Booking model

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    property = models.ForeignKey(Stay, on_delete=models.PROTECT, null=True)
    checkin = models.DateField(null=True)
    checkout = models.DateField(null=True,)

    def __str__(self) -> str:
        return self.property.title
    