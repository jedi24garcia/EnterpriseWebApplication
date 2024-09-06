from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.UserLogin, name='login'),
    path('signup/', views.UserSignUp, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]