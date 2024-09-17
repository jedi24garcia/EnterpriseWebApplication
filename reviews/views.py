from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Review

# Create your views here.
# Review List View
class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

# Review Detail View
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'