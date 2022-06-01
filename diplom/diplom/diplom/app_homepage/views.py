from django.shortcuts import render
from app_tasks.models import *


def homepage(request):
    tasks = TaskModel.objects.all()
    return render(request, 'app_homepage/homepage.html', context={'tasks': tasks})
