from django.urls import path
from .views import all_doctors, volteneer_doctors
app_name = 'doctors_app'

urlpatterns = [
    path('doctors/', all_doctors, name='all'),
    path('volteneer/', volteneer_doctors, name='volteneer'),
]
