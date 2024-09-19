from django.shortcuts import render, redirect
from .forms import BookingForm
from reviews.views import review_view
# from django.views.generic import ListView
# from .models import Booking

# Create your views here.
# Booking form view
def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect(review_view)
        
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {"form": form})

# Booking List View
# class BookingListView(ListView):
#    model = Booking
#    template_name = 'bookings/booking_list.html'
#    context_object_name = 'bookings'