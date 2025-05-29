from django.shortcuts import render
from .models import Appointment

def about(request):
    return render(request, 'base.html')

def appointments(request):
    all_appointments = Appointment.objects.select_related('animal').all()
    return render(request, 'app.html', {
        'appointments': all_appointments
    })