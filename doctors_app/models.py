from django.db import models


class DoctorsSpecialist(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class VoltDoctors(models.Model):
    CHOICES = (
        ('مساءًا', 'مساءًا'),
        ('صباحًا', 'صباحًا'),
    )
    name = models.CharField(max_length=150)
    specialist = models.ForeignKey(DoctorsSpecialist, on_delete=models.CASCADE)
    mobile_num = models.CharField(max_length=150)
    from_time = models.CharField(max_length=50)
    to_time = models.CharField(max_length=50)
    from_per = models.CharField(choices=CHOICES, max_length=50)
    to_per = models.CharField(choices=CHOICES, max_length=50)

    def __str__(self):
        return self.name
