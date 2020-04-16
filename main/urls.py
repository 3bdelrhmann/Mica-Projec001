from django.urls import path
from .views import HomePage, symptoms, about

app_name = 'main'

urlpatterns = [
    path('symptoms/', symptoms, name='symptoms'),
    path('', HomePage, name='main'),
    path('about/', about, name='about'),
]
