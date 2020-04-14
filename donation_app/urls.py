from django.urls import path
from .views import organizations, people_donation
app_name = 'donation_app'

urlpatterns = [
    path('organizations', organizations, name='organization'),
    path('peoples', people_donation, name='peoples'),
]
