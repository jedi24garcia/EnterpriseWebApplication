from django.urls import path
from bookings import views
# from .views import BookingListView

# urls for Bookings

urlpatterns = [
    path('form/', views.booking_view, name='booking_form'),
#   path('bookings/', BookingListView.as_view(), name='booking_list'),
]