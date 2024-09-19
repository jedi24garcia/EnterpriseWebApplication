from django.shortcuts import render, redirect
from .forms import ReviewForm
# from django.views.generic import ListView, DetailView
# from .models import Review

# Create your views here.
# Review form view
def review_view(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("home")
        
    else:
        form = ReviewForm()

    return render(request, "reviews/review_form.html", {"form": form})

# Review List View
# class ReviewListView(ListView):
#    model = Review
#    template_name = 'reviews/review_list.html'
#    context_object_name = 'reviews'

# Review Detail View
# class ReviewDetailView(DetailView):
#    model = Review
#    template_name = 'reviews/review_detail.html'
#    context_object_name = 'review'