from django.shortcuts import render
from .models import PeoplesDonation, OrganizationsDonation


def organizations(request):

    queryset = OrganizationsDonation.objects.all()
    conext = {
        'orgs': queryset,
     'title' : ' دعم الؤسسات  الخيرية',

    }
    return render(request, 'donation_app/org.html', conext)


def people_donation(request):
    queryset = PeoplesDonation.objects.all()

    conext = {
        'peoples': queryset,
             'title' : ' دعم العماله اليومية',

    }

    return render(request, 'donation_app/peoples.html', conext)
