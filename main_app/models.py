from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250)
    carrier = models.CharField(max_length=250)
    review = models.TextField(max_length=250)

    def __self__(self):
        return self.name
