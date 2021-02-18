# import models class from django
from django.forms import ModelForm

# import models (Usage)
from .models import Usage

class UsageForm(ModelForm):
    class Meta:
        model = Usage
        fields = ['date', 'time', 'usage']
