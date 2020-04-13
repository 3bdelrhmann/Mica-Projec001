from django.urls import path
from .views import volteneerDoctors
app_name = 'doctors_app'
urlpatterns = [
    path('volteneer/', volteneerDoctors, name='volteneer-doctors'),
]
