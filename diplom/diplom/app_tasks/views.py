from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import *
from .forms import *
from django.views.generic.edit import CreateView


def tasks(request):
    tags = Tag.objects.all()
    return render(request, 'app_tasks/tasks.html', context={'tags': tags})


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
