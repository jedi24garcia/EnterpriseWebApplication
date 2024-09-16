from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



# Register your models here.

admin.site.register(Profile)

# Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name"]
    inlines = [ProfileInline]

#Customise a user list on the admin page

UserAdmin.list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')

#Unregisted the old way

admin.site.unregister(User)

#Re-Register the new way
admin.site.register(User, UserAdmin)
