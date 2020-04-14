from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)
    city = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.name


class CovidStats(models.Model):
    total_cases = models.IntegerField()
    total_deaths = models.IntegerField()
    total_recoverd = models.IntegerField()

    new_confirmed = models.IntegerField()
    new_recovered = models.IntegerField()
    new_deaths = models.IntegerField()

    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.last_update)
