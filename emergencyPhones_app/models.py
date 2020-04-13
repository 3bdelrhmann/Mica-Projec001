from django.db import models


class EmergencyPhone(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name
