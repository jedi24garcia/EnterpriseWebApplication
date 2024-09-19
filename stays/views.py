from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Stay, Host
from bookings.forms import BookingForm

# List view for stays
class StayListView(ListView):
    model = Stay
    template_name = 'stays/stay_list.html'
    context_object_name = 'stays'

# Detail view for stays
class StayDetailView(DetailView):
    model = Stay
    template_name = 'stays/stay_detail.html'
    context_object_name = 'stay'

    # Display form on stay detail
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingForm()
        return context
    
    # Process form
    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # Get stay being displayed
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.stay = self.object
            booking.user = request.user
            booking.save()
            return redirect('home')
        
        #if form is invalid

# List view for hosts
class HostListView(ListView):
    model = Host
    template_name = 'stays/host_list.html'
    context_object_name = 'hosts_'

# Detail view for hosts
class HostDetailView(DetailView):
    model = Host
    template_name = 'stays/host_detail.html'
    context_object_name = 'host'