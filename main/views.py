from django.shortcuts import render
from django.utils import timezone
import requests
from .models import CovidStats
import datetime

today = timezone.now()


def HomePage(request):
    period = 'مساءًا'
    get_stats = CovidStats.objects.all().first()
    api_url = 'https://api.smartable.ai/coronavirus/stats/global'

    headers = {
        'Cache-Control': 'no-cache',
        'Subscription-Key': '978fb85af3f740599b792308320a56aa',
    }
    if not get_stats:

        response = requests.get(headers=headers, url=api_url)
        data = response.json()

        create_obj = CovidStats.objects.create(
            total_cases=data['stats']['totalConfirmedCases'],
            total_deaths=data['stats']['totalDeaths'],
            total_recoverd=data['stats']['totalRecoveredCases'],
            new_confirmed=data['stats']['newlyConfirmedCases'],
            new_recovered=data['stats']['newlyRecoveredCases'],
            new_deaths=data['stats']['newDeaths'],
            counter=1,
        )
        create_obj.save()
        totalCases = data['stats']['totalConfirmedCases']
        totalRecovered = data['stats']['totalDeaths']
        totalDeaths = data['stats']['totalRecoveredCases']
        new_confirmed = data['stats']['newlyConfirmedCases']
        new_recovered = data['stats']['newlyRecoveredCases']
        new_deaths = data['stats']['newDeaths']
    else:
        last_update = get_stats.last_update
        a = today - last_update
        if a.total_seconds() > 3600:
            response = requests.get(headers=headers, url=api_url)
            data = response.json()
            get_stats.total_cases = data['stats']['totalConfirmedCases']
            get_stats.total_deaths = data['stats']['totalDeaths']
            get_stats.total_recoverd = data['stats']['totalRecoveredCases']
            get_stats.new_confirmed = data['stats']['newlyConfirmedCases']
            get_stats.new_recovered = data['stats']['newlyRecoveredCases']
            get_stats.new_deaths = data['stats']['newDeaths']
            get_stats.counter += 1
            get_stats.save()

        totalCases = get_stats.total_cases
        totalRecovered = get_stats.total_recoverd
        totalDeaths = get_stats.total_deaths
        new_confirmed = get_stats.new_confirmed
        new_recovered = get_stats.new_recovered
        new_deaths = get_stats.new_deaths
    if get_stats.last_update.strftime('%p') == 'AM':
        period = 'صباحًا'
    context = {
        'new_confirmed': new_confirmed,
        'new_recovered': new_recovered,
        'new_deaths': new_deaths,
        'period': period,
        'last_update': get_stats.last_update,
        'totalCases': totalCases,
        'totalRecovered': totalRecovered,
        'totalDeaths': totalDeaths,
        'countries': 120,
        'title': 'الصفحة الرئيسية',
    }
    return render(request, 'main/index.html', context)


def symptoms(request):
    context = {
     'title' : ' الأعراض',

    }
    return render(request, 'main/symptoms.html', context)


def about(request):
    context = {
        'title' : ' اِحنا مين',

    }
    return render(request, 'main/about.html', context)
