from django.db import models
from main.models import City


class Labs(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.hospital_name
