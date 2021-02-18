from django.db import models
from django.urls import reverse
from datetime import date

USAGES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class Phone(models.Model):
    name = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250)
    carrier = models.CharField(max_length=250)
    review = models.TextField(max_length=250)

    def __self__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone_detail', kwargs={'phone_id': self.id})


class Case(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __self__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('case_detail', kwargs={'pk': self.id})
    
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
