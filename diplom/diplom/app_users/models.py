from django.contrib.auth.models import User
from django.db import models


class ProfileModel(models.Model):
    STATUS_CHOICES = [('co', 'contractor'),
                      ('cu', 'customer'),
                      ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_status = models.CharField(max_length=2, choices=STATUS_CHOICES)


class ProfileContractorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_img/', blank=True)
    # rating =
    birth_day = models.DateField(blank=True, default='2000-01-01')
    phone = models.CharField(blank=True, max_length=15)
    city = models.CharField(blank=True, max_length=30)
    university = models.CharField(blank=True, max_length=50)
    faculty = models.CharField(blank=True, max_length=50)
    specialization = models.CharField(blank=True, max_length=50)


class ProfileCustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_img/', blank=True)
    company = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=15)
    city = models.CharField(blank=True, max_length=50)


