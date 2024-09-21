from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Stay, Host
from bookings.forms import BookingForm
from django.http import HttpResponseForbidden

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import HostRegiForm, HostProfileForm
from django.contrib import messages
from django import forms

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

# Update stay
class StayUpdateView(UpdateView):
    model = Stay
    fields = ['title', 'price', 'location', 'guests', 'bedrooms', 'bathrooms', 'features', 'description', 'address']
    template_name = 'stays/stay_form.html'
    success_url = '/'
    
    # def get_object(self, queryset=None):
    #     stay = super().get_object(queryset)
    #     user = self.request.user
    #     if stay.host.user == user:
    #         return stay
    #     else:
    #         raise HttpResponseForbidden("You can not edit this stay.")
        
# Delete View
class StayDeleteView(DeleteView):
    model = Stay
    success_url = '/'
    template_name = 'stays/stay_confirm_delete.html'

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

# Host profile and edit
@login_required
def hostprofile(request):
    if request.method == 'POST':
        h_form = HostRegiForm(request.POST, instance=request.user.host)
        hp_form = HostProfileForm(request.POST,
                                    request.FILES,
                                    instance=request.user.host)

        if h_form.is_valid() and hp_form.is_valid():
            h_form.save()
            hp_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('host_profile')
    
    else:
        h_form = HostRegiForm(instance=request.user.host)
        hp_form = HostProfileForm(instance=request.user.host)
    

    context = {
        'h_form': h_form,
        'hp_form': hp_form
    }

    return render(request, 'stays/host_profile.html', context)