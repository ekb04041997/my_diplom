# Generated by Django 3.2.13 on 2022-06-14 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileCustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, upload_to='profile_img/')),
                ('company', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Работодатель',
                'verbose_name_plural': 'Работодатели',
            },
        ),
        migrations.CreateModel(
            name='ProfileContractorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, upload_to='profile_img/')),
                ('birth_day', models.DateField(blank=True, default='2000-01-01')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('university', models.CharField(blank=True, max_length=50)),
                ('faculty', models.CharField(blank=True, max_length=50)),
                ('specialization', models.CharField(blank=True, max_length=50)),
                ('rating', models.IntegerField(default=0)),
                ('count_task', models.IntegerField(default=0)),
                ('middle_point', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'ordering': ['-rating'],
            },
        ),
    ]
