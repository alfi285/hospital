from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments
from .models import Doctors

from .form import BookingForm

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,  # From
            ['alfiyazon@gmail.com'],  # To (change this!)
            fail_silently=False,
        )
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})




def department_view(request):    
    dict_dept = {
    'dept':Departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)

def doctors_view(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)

