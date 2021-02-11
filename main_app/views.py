from django.shortcuts import render
from .models import Phone


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def phone_index(request):
    phones = Phone.objects.all()
    return render(request, 'phones/index.html', {'phones': phones})

def phone_detail(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    return render(request, 'phones/detail.html', {'phone': phone})