from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


USAGES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class Case(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __self__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('case_detail', kwargs={'pk': self.id})

class Phone(models.Model):
    name = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250)
    carrier = models.CharField(max_length=250)
    review = models.TextField(max_length=250)
    cases = models.ManyToManyField(Case)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __self__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone_detail', kwargs={'phone_id': self.id})
 
class Usage(models.Model):
    date = models.DateField('usage date')
    usage = models.CharField(
        max_length=1,
        choices=USAGES,
        default=USAGES[0][0],
    )
    time = models.CharField(max_length=1)

    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_usage_display()} at {self.date} for {self.time} hours"
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for phone.id: {self.phone_id} @{self.url}"