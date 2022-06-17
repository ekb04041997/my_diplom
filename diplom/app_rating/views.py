from django.shortcuts import render
from app_tasks.models import *
from app_users.models import *
from django.core.paginator import Paginator


def rating_all(request):
    tags = Tag.objects.all()
    users = ProfileContractorModel.objects.filter(rating__gt=0)

    top_users = []
    for place, user in enumerate(users):
        user.place = place + 1
        top_users.append(user)

    paginator = Paginator(top_users, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_rating/rating.html', context={'top_users': top_users,
                                                              'tags': tags,
                                                              'page_obj': page_obj,
                                                              })


def rating_for_category(request, pk):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=pk)
    users = ContractorTag.objects.filter(tag=tag)

    top_users = []
    for place, user in enumerate(users):
        user.place = place + 1
        top_users.append(user)

    paginator = Paginator(top_users, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_rating/rating.html', context={'tags': tags,
                                                              'tag': tag,
                                                              'top_users': top_users,
                                                              'page_obj': page_obj,
                                                              })