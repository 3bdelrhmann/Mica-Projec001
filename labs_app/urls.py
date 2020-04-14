from django.urls import path
from .views import labs, LabsView
app_name = 'labs_app'

urlpatterns = [
    path('', LabsView.as_view(), name='all')
]
