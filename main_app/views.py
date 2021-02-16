from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Phone, Case


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def phones_index(request):
    phones = Phone.objects.all()
    return render(request, 'phones/index.html', {'phones': phones})

def phone_detail(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    return render(request, 'phones/detail.html', {'phone': phone})

class PhoneCreate(CreateView):
    model = Phone
    fields = '__all__'

class PhoneUpdate(UpdateView):
    model = Phone
    fields = ['review', 'carrier']

class PhoneDelete(DeleteView):
    model = Phone
    success_url = '/phones/'

# Case Views
def cases_index(request):
    cases = Case.objects.all()
    return render(request, 'cases/index.html', {'cases': cases})

def case_detail(request, case_id):
    case = Case.objects.get(id=case_id)
    return render(request, 'cases/detail.html', {'case': case})

class CaseCreate(CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(UpdateView):
    model = Case
    fields = ['name', 'color']

class CaseDelete(DeleteView):
    model = Case
    success_url = '/cases/'