from django.shortcuts import render
from app_tasks.models import *
from app_users.models import *


def homepage(request):
    tasks = TaskModel.objects.all()
    users = ProfileContractorModel.objects.filter(rating__gt=0)
    top_users = []
    for place, user in enumerate(users):
        user.place = place + 1
        top_users.append(user)
    return render(request, 'app_homepage/homepage.html', context={'tasks': tasks,
                                                                  'top_users': top_users})
