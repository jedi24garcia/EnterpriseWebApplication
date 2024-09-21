from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

# Create Customer Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email_address = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to="profile_pics")
        

    def __str__(self):
        return self.user.username



