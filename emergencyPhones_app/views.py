from django.shortcuts import render
from .models import EmergencyPhone


def emergency_numbers(request):
    queryset = EmergencyPhone.objects.all()
    context = {
        'numbers': queryset, 
        'title' : ' ارقام الطوارئ',

    }
    return render(request, 'emergencyPhones_app/numbers.html', context)
