from django.urls import path
from .views import ReviewListView, ReviewDetailView

# urls for Reviews
urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
]