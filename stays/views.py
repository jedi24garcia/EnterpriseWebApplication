from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stay, Host

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

