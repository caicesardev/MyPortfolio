from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import *


def home(request):
    context = {}
    return render(request, 'portfolio/home.html')


def portfolio(request):
    context = {}
    return render(request, 'portfolio/portfolio.html')


def about(request):
    context = {}
    return render(request, 'portfolio/about.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = f"Nuevo mensaje de: {data['name']} | {data['email']} \n \nMensaje: {data['message']}"

        send_mail(data['subject'], message,
                  settings.EMAIL_HOST_USER, ['caicesardev@gmail.com'], fail_silently=False)

    context = {}
    return render(request, 'portfolio/contact.html')


def blog(request):
    context = {}
    return render(request, 'portfolio/blog.html')
