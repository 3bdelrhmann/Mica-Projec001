from django.urls import path
from .views import HomePage
app_name = 'main'

urlpatterns = [
    path('', HomePage, name='home')
]
