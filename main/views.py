from django.shortcuts import render
from django.utils import timezone
import requests


today = timezone.now()


def HomePage(request):

    countries = 200
    totalCases = 15
    totalDeaths = 15
    totalRecovered = 15
    context = {
        'today': today,
        'totalCases': totalCases,
        'totalRecovered': totalRecovered,
        'totalDeaths': totalDeaths,
        'countries': countries,
        'title': 'الصفحة الرئيسية',
    }
    return render(request, 'main/index.html', context)
