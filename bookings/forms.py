from django import forms
from .models import Booking

# Date input widget
class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'property', 'checkin', 'checkout')

        widgets = {
            'checkin': DateInput(attrs={'class': 'form_control', 'placeholder': 'Select a check-in date'}),
            'checkout': DateInput(attrs={'class': 'form_control', 'placeholder': 'Select a check-out date'}),
        }