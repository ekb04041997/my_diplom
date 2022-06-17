from django.contrib import admin
from django.utils.html import format_html

from .models import *

admin.site.register(Tag)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'Заголовок', 'Задание', 'files']

    def Заголовок(self, obj):
        from django.db.models import Avg
        result = TaskModel.objects.filter(id=obj.id).aggregate(Avg("title"))
        if len(obj.title) > 20:
            return format_html("{}...", obj.title[:20])
        return obj.title

    def Задание(self, obj):
        from django.db.models import Avg
        result = TaskModel.objects.filter(id=obj.id).aggregate(Avg("content"))
        if len(obj.content) > 100:
            return format_html("{}...", obj.content[:100])
        return obj.content


class ContractorTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'task', 'point', 'pub_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment']


class ContractorTagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'user']


admin.site.register(TaskModel, TaskAdmin)
admin.site.register(ContractorTask, ContractorTaskAdmin)
admin.site.register(Comment)
admin.site.register(CustomerTag)
admin.site.register(ContractorTag,ContractorTagAdmin)
