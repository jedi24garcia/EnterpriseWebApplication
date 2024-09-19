from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    
    checkin = forms.DateField(widget=forms.SelectDateWidget)
    checkout = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Booking
        fields = ['checkin', 'checkout']