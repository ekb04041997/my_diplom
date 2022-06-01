from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from random import randint
from django.contrib.auth.models import User
import datetime


class TaskModel(models.Model):
    # db_index=True use for initial in bd for fast search
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasksmodels', verbose_name='Пользователь')
    title = models.CharField(max_length=150, db_index=True)
    content = models.TextField(max_length=1500, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')
    files = models.FileField(upload_to="task_files/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tasks'
        ordering = ['-pub_date']


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
