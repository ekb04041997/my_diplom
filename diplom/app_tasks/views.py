from django.shortcuts import render, redirect
from django.views.generic import DetailView

from app_users.models import *
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from django.utils import timezone


def tasks(request):
    tags = Tag.objects.all()
    tasks = TaskModel.objects.all()
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/tasks.html', context={'tags': tags,
                                                            'page_obj': page_obj
                                                            })


def customer_tasks(request, user_id):
    temp_user = User.objects.get(id=user_id)
    tags = Tag.objects.all()
    tasks = TaskModel.objects.filter(user=temp_user)
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/customer_tasks.html', context={'tags': tags,
                                                                 'page_obj': page_obj,
                                                                 'user_info': temp_user,
                                                                 })


def contractor_tasks(request, user_id):
    temp_user = User.objects.get(id=user_id)
    tags = Tag.objects.all()
    tasks = ContractorTask.objects.filter(user=temp_user, point__gt=0)
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/contractor_tasks.html', context={'tags': tags,
                                                                 'page_obj': page_obj,
                                                                 'user_info': temp_user,
                                                                 })


def customer_tag_detail(request, user_id, pk):
    temp_user = User.objects.get(id=user_id)
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=pk)
    tasks = TaskModel.objects.filter(user=temp_user, tags=tag)
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/customer_tasks.html', context={'tags': tags,
                                                                 'tag': tag,
                                                                 'page_obj': page_obj,
                                                                 'user_info': temp_user,
                                                                 })


def contractor_tag_detail(request, user_id, pk):
    temp_user = User.objects.get(id=user_id)
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=pk)
    tasks = ContractorTask.objects.filter(user=temp_user, point__gt=0, task__tags=tag)
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/contractor_tasks.html', context={'tags': tags,
                                                                       'tag': tag,
                                                                       'page_obj': page_obj,
                                                                       'user_info': temp_user,
                                                                       })


class TaskCreateView(CreateView):
    model = TaskModel
    fields = ['title', 'content', 'tags', 'files']
    template_name = 'app_tasks/task_create.html'

    def post(self, request, *args, **kwargs):
        temp_task = TaskForm(request.POST, request.FILES)
        temp_task.tags = Tag.objects.get(id=request.POST['tags'])

        if temp_task.is_valid():
            task_model = temp_task.save(commit=False)
            task_model.user = request.user
            task_model.save()

            if CustomerTag.objects.filter(tag=temp_task.tags, user=request.user):
                cu_tag = CustomerTag.objects.get(tag=temp_task.tags, user=request.user)
                cu_tag.count_task += 1
                cu_tag.save()
            else:
                CustomerTag.objects.create(tag=temp_task.tags, user=request.user, count_task=1)

            return redirect('task_detail', pk=task_model.id)

        return redirect('homepage')


class TaskDetailView(DetailView):
    model = TaskModel
    template_name = 'app_tasks/task_detail.html'


def tag_detail(request, pk):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=pk)
    tasks = TaskModel.objects.filter(tags=tag)
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/tasks.html', context={'tags': tags,
                                                            'tag': tag,
                                                            'page_obj': page_obj,
                                                            })


def contractor_chat(request, user_id):
    user = User.objects.get(id=user_id)
    comment_form = ContractorCommentForm()

    if request.method == "POST":
        form = ContractorCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment_model = form.save(commit=False)
            comment_model.user = request.user
            comment_model.task = ContractorTask.objects.get(id=request.POST['task'])
            comment_model.save()

    tasks = ContractorTask.objects.filter(user=user)
    chat = []
    for task in tasks:
        chat.append(task.task)
    return render(request, 'app_tasks/chat_contractor.html', context={'tasks': tasks,
                                                                      'chat': chat,
                                                                      'comment_form': comment_form})


def customer_chat(request, user_id):
    user = User.objects.get(id=request.user.id)
    comment_form = CustomerCommentForm()
    marks = [i for i in range(1, 11)]

    if request.method == "POST":
        form_comment = ContractorCommentForm(request.POST)
        form_point = ContractorTaskForm(request.POST)

        if form_point.is_valid():
            co_user = User.objects.get(id=request.POST['user_id'])
            task = TaskModel.objects.get(contractortasks__id=request.POST['task_id'])
            temp_task = ContractorTask.objects.get(id=request.POST['task_id'])
            temp_task.point = request.POST['point']
            temp_task.close_time = timezone.now()
            temp_task.save()

            profile = ProfileContractorModel.objects.get(user=co_user)
            profile.rating += int(request.POST['point'])
            profile.count_task += 1
            profile.middle_point = round(profile.rating / profile.count_task, 2)
            profile.save()

            if ContractorTag.objects.filter(tag__id=task.tags.id, user=co_user):
                co_tag = ContractorTag.objects.get(tag=task.tags, user=co_user)
                co_tag.count_task += 1
                co_tag.all_point += int(request.POST['point'])
                co_tag.middle_point = round(co_tag.all_point / co_tag.count_task, 2)
                co_tag.save()
            else:
                ContractorTag.objects.create(tag=temp_task.task.tags,
                                             user=co_user,
                                             count_task=1,
                                             all_point=int(request.POST['point']),
                                             middle_point=int(request.POST['point'])/1,
                                             )

            comment = f'Ваше задание принято.\nОценка: {request.POST["point"]}'
            user = request.user
            Comment.objects.create(task=temp_task, user=user, comment=comment)



        if form_comment.is_valid():
            comment_model = form_comment.save(commit=False)
            comment_model.user = request.user
            comment_model.task = ContractorTask.objects.get(id=request.POST['task'])
            comment_model.save()

    tasks = TaskModel.objects.filter(user=user)

    task_users = []
    co_task = []
    for task in tasks:
        if ContractorTask.objects.filter(task=task):
            temp_users = ContractorTask.objects.filter(task=task)
            users = []
            for user in temp_users:
                user.user.id_task = task.id
                users.append(user.user)
                temp_co_task = ContractorTask.objects.get(task__id=task.id, user=user.user)
                co_task.append(temp_co_task)
            task_users.append((users, task.id))

    return render(request, 'app_tasks/chat_customer.html', context={'tasks': tasks,
                                                                    'task_users': task_users,
                                                                    'co_task': co_task,
                                                                    'comment_form': comment_form,
                                                                    'marks': marks})


def add_contractor_task(request, user_id, task_id):
    user = User.objects.get(id=user_id)
    task = TaskModel.objects.get(id=task_id)
    if not ContractorTask.objects.filter(user=user, task=task):
        ContractorTask.objects.create(user=user, task=task)

    return redirect('contractor_chat', user_id)
