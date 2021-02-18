from django.contrib import admin
from .models import Phone, Case, Usage
# Register your models here.
admin.site.register(Phone)
admin.site.register(Case)
admin.site.register(Usage)