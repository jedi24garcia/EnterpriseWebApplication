from django.urls import path
from reviews import views
# from .views import ReviewListView, ReviewDetailView

# urls for Reviews
urlpatterns = [
    path('form/', views.review_view , name='review_form'),
]