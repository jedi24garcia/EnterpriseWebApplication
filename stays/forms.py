from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Host


class HostRegiForm(forms.ModelForm):

    hosting_years = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Hosting Years'}), required=False)
    about = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'About'}), required=False)
    class Meta:
        model = Host
        fields =['hosting_years', 'about']



class HostProfileForm(forms.ModelForm):

    class Meta:
        model = Host
        fields =['host_pic']

