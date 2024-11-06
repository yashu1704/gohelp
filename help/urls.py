from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('service_providers/', views.service_provider_list, name='service_provider_list'),
    path('service_history/', views.service_history_list, name='service_history_list'),
]