from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.UserLogin, name='login'),
    path('signup/', views.UserSignUp, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_profile/', views.profile, name='user_profile'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)