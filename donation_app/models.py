from django.db import models
from main.models import City


class PeoplesDonation(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class OrganizationsDonation(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    logo = models.ImageField(upload_to='images/organizations/')

    def __str__(self):
        return self.name
