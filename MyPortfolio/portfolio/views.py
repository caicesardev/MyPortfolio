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

    context = {}
    return render(request, 'portfolio/contact.html')


def blog(request):
    context = {}
    return render(request, 'portfolio/blog.html')
