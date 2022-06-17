from django.contrib.auth.models import User
from django.db import models


class ProfileContractorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_img/', blank=True)
    birth_day = models.DateField(blank=True, default='2000-01-01')
    phone = models.CharField(blank=True, max_length=15)
    city = models.CharField(blank=True, max_length=30)
    university = models.CharField(blank=True, max_length=50)
    faculty = models.CharField(blank=True, max_length=50)
    specialization = models.CharField(blank=True, max_length=50)

    rating = models.IntegerField(default=0)
    count_task = models.IntegerField(default=0)
    middle_point = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['-rating']


class ProfileCustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_img/', blank=True)
    company = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=15)
    city = models.CharField(blank=True, max_length=50)

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'

