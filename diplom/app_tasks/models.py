from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasksmodels', verbose_name='Пользователь')
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок')
    content = models.TextField(max_length=1500, db_index=True, verbose_name='Задание')
    pub_date = models.DateTimeField(auto_now_add=True)

    tags = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='tasks')
    files = models.FileField(upload_to="task_files/", blank=True, verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tasks'
        ordering = ['-pub_date']
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Tag(models.Model):
    title = models.CharField(max_length=30, verbose_name='Тег')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class ContractorTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contractortasks')
    task = models.ForeignKey('TaskModel', on_delete=models.CASCADE, related_name='contractortasks')
    point = models.IntegerField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    close_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-close_time']

class Comment(models.Model):
    task = models.ForeignKey('ContractorTask', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=1500, verbose_name='Комментарий')
    file = models.FileField(upload_to="comment_files/", blank=True, verbose_name='Файл')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.comment


class CustomerTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='customertags')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customertags')
    count_task = models.IntegerField(default=0)

    class Meta:
        db_table = 'CustomerTag'
        ordering = ['user']
        verbose_name = 'Теги работодателя'
        verbose_name_plural = 'Теги работодателей'


class ContractorTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='contractortags')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contractortags')
    all_point = models.IntegerField(default=0)
    count_task = models.IntegerField(default=0)
    middle_point = models.FloatField(default=0)

    class Meta:
        db_table = 'ContractorTag'
        ordering = ['-all_point']
        verbose_name = 'Теги исполнителя'
        verbose_name_plural = 'Теги исполнителей'
