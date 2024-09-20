from django.urls import path
from .views import StayListView, StayDetailView, HostListView, HostDetailView, StayUpdateView, StayDeleteView

# urls for stays
urlpatterns = [
    path("", StayListView.as_view(), name='home'),
    path('stays/', StayListView.as_view(), name='stay_list'),
    path('stays/<int:pk>', StayDetailView.as_view(), name='stay_detail'),
    path('stays/<int:pk>/edit/', StayUpdateView.as_view(), name='stay_edit'),
    path('stays/<int:pk>/delete/', StayDeleteView.as_view(), name='stay_delete'),
    path('hosts/', HostListView.as_view(), name='host_list'),
    path('hosts/<int:pk>', HostDetailView.as_view(), name='host_detail'),
]