from django.urls import path
from .views import BookingListView

# urls for Bookings

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='booking_list'),
]