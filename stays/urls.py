from django.urls import path
from .views import StayListView, StayDetailView, HostListView, HostDetailView

# urls for stays
urlpatterns = [
    path("", StayListView.as_view(), name='home'),
    path('stays/', StayListView.as_view(), name='stay_list'),
    path('stays/<int:pk>', StayDetailView.as_view(), name='stay_detail'),
    path('hosts/', HostListView.as_view(), name='host_list'),
    path('hosts/<int:pk>', HostDetailView.as_view(), name='host_detail'),
]

