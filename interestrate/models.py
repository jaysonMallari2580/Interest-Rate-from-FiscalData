from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Interestrate(models.Model):
    rate_date = models.DateField()
    rate_value = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):
        return self.rate_value