from django.shortcuts import render, redirect
from .models import VoltDoctors
from .forms import DocForm
from django.contrib import messages


def all_doctors(request):
    queryset = VoltDoctors.objects.all()
    context = {
        'doctors': queryset,
    }

    return render(request, 'doctors_app/doctors.html', context)


def volteneer_doctors(request):
    form = DocForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافتك إلي فريق  الأطباء المتطوعين')
            return redirect('doctors:all')
    context = {
        'form': form,
    }

    return render(request, 'doctors_app/doctorform.html', context)
