from django.urls import path
from .views import HomePage, symptoms

app_name = 'main'

urlpatterns = [
    path('symptoms/', symptoms, name='symptoms'),
    path('', HomePage, name='main')
]
