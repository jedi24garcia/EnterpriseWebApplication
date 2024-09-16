from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

  first_name = forms.CharField(max_length=40, required=True, help_text='Enter your first name')
  first_name = forms.CharField(max_length=40, required=True, help_text='Enter your last name')

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)