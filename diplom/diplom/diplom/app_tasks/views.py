from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator


def tasks(request):
    tags = Tag.objects.all()
    tasks = TaskModel.objects.all()
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/tasks.html', context={'tags': tags,
                                                            'page_obj': page_obj
                                                            })


def user_tasks(request, user_id):
    temp_user = User.objects.get(id=user_id)
    tags = Tag.objects.all()
    tasks = TaskModel.objects.filter(user=temp_user)
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/user_tasks.html', context={'tags': tags,
                                                            'page_obj': page_obj,
                                                            'user_info': temp_user,
                                                            })


class TaskCreateView(CreateView):
    model = TaskModel
    fields = ['title', 'content', 'tags', 'files']
    template_name = 'app_tasks/task_create.html'

    def post(self, request, *args, **kwargs):
        temp_task = TaskForm(request.POST, request.FILES)

        if temp_task.is_valid():
            task_model = temp_task.save(commit=False)
            task_model.user = request.user
            task_model.save()

            # Добавление модели Tag со связью m2m с текущей моделью задания.
            task_model.tags.add(*temp_task.cleaned_data["tags"])
            task_model.save()

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


def user_tag_detail(request, user_id, pk):
    temp_user = User.objects.get(id=user_id)
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=pk)
    tasks = TaskModel.objects.filter(user=temp_user, tags=tag)
    paginator = Paginator(tasks, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_tasks/user_tasks.html', context={'tags': tags,
                                                                 'tag': tag,
                                                                 'page_obj': page_obj,
                                                                 'user_info': temp_user,
                                                                 })
