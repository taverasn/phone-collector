import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsageForm
from .models import Phone, Case, Photo

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'taveras-phonecollector'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('phones_index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def phones_index(request):
    # phones = Phone.objects.all()
    phones = Phone.objects.filter(user=request.user)
    return render(request, 'phones/index.html', {'phones': phones})


@login_required
def phone_detail(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    cases_phone_doesnt_have = Case.objects.exclude(id__in=phone.cases.all().values_list('id'))
    usage_form = UsageForm()
    return render(request, 'phones/detail.html', {
        'phone': phone,
        'usage_form': usage_form,
        'cases': cases_phone_doesnt_have,
        })


@login_required
def add_usage(request, phone_id):
    form = UsageForm(request.POST)
    if form.is_valid():
        new_usage = form.save(commit=False)
        new_usage.phone_id = phone_id
        new_usage.save()
    return redirect('phone_detail', phone_id=phone_id)


@login_required
def assoc_case(request, phone_id, case_id):
    Phone.objects.get(id=phone_id).cases.add(case_id)
    return redirect('phone_detail', phone_id=phone_id)

@login_required
def unassoc_case(request, phone_id, case_id):
    Phone.objects.get(id=phone_id).cases.remove(case_id)
    return redirect('phone_detail', phone_id=phone_id)

@login_required
def add_photo(request, phone_id):
    photo_file = request.FILES.get('photo_file', None)

    if photo_file:
        s3 = boto3.client('s3')

        index_of_last_period = photo_file.name.rfind('.')
        key = uuid.uuid4().hex[:6] + photo_file.name[index_of_last_period]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)

            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url=url, phone_id=phone_id)
            photo.save()
        except:
            print('An error occured uploading file to S3 AWS')
    return redirect('phone_detail', phone_id=phone_id)

class PhoneCreate(LoginRequiredMixin, CreateView):
    model = Phone
    fields = ['name', 'manufacturer', 'carrier', 'review']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class PhoneUpdate(LoginRequiredMixin, UpdateView):
    model = Phone
    fields = ['review', 'carrier']

class PhoneDelete(LoginRequiredMixin, DeleteView):
    model = Phone
    success_url = '/phones/'

# Case Views
class CaseList(LoginRequiredMixin, ListView):
    model = Case

class CaseDetail(LoginRequiredMixin, DetailView):
    model = Case
    fields = '__all__'

class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ['name', 'color']

class CaseDelete(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = '/cases/'
