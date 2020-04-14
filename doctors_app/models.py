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
    name = models.CharField(max_length=150, blank=False, null=False)
    specialist = models.ForeignKey(
        DoctorsSpecialist, on_delete=models.CASCADE, blank=False, null=False)
    mobile_num = models.CharField(max_length=150, blank=False, null=False)
    from_time = models.CharField(max_length=50, blank=False, null=False)
    to_time = models.CharField(max_length=50, blank=False, null=False)
    from_per = models.CharField(
        choices=CHOICES, max_length=50, blank=False, null=False)
    to_per = models.CharField(
        choices=CHOICES, max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
