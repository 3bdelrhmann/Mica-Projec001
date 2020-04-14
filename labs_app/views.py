from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse
from .models import Labs
from django.views.generic import ListView


class LabsView(ListView):
    model = Labs
    template_name = 'labs_app/labs.html'
    context_object_name = 'labs'
    paginate_by = 1
    queryset = Labs.objects.all()


def labs(request):

    return render(request, 'labs_app/labs.html')
