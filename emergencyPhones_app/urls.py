from django.urls import path
from .views import emergency_numbers
app_name = 'emergencyPhones_app'

urlpatterns = [
    path('', emergency_numbers),
]
