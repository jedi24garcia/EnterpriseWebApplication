from django.db import models
from django.contrib.auth.models import User
from stays.models import Stay

# Create your models here.
# Booking model

class Booking(models.Model):
    stay = models.ForeignKey(Stay, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    checkin = models.DateField()
    checkout = models.DateField()
    

    def __str__(self) -> str:
        return f'{self.stay.title}, reservation for {self.user.last_name}'
    