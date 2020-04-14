from django.contrib import admin
from .models import PeoplesDonation, OrganizationsDonation

admin.site.register(PeoplesDonation)
admin.site.register(OrganizationsDonation)
