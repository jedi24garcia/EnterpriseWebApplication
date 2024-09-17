from django.shortcuts import render
from django.views.generic import ListView
from .models import Booking

# Create your views here.
# Booking List View

class BookingListView(ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'