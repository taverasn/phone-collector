from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Phone, Case
from .forms import UsageForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def phones_index(request):
    phones = Phone.objects.all()
    return render(request, 'phones/index.html', {'phones': phones})

def phone_detail(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    usage_form = UsageForm()
    return render(request, 'phones/detail.html', {
        'phone': phone, 'usage_form': usage_form
        })

def add_usage(request, phone_id):
    form = UsageForm(request.POST)
    if form.is_valid():
        new_usage = form.save(commit=False)
        new_usage.phone_id = phone_id
        new_usage.save()
    return redirect('phone_detail', phone_id=phone_id)

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
class CaseList(ListView):
    model = Case

class CaseDetail(DetailView):
    model = Case
    fields = '__all__'

class CaseCreate(CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(UpdateView):
    model = Case
    fields = ['name', 'color']

class CaseDelete(DeleteView):
    model = Case
    success_url = '/cases/'