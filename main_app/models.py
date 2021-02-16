from django.db import models
from django.urls import reverse

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
        return reverse('case_detail', kwargs={'case_id': self.id})
