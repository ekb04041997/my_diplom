from django.contrib import admin
from django.utils.html import format_html

from .models import *

admin.site.register(Tag)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'show_title', 'show_content', 'files']

    def show_title(self, obj):
        from django.db.models import Avg
        result = TaskModel.objects.filter(id=obj.id).aggregate(Avg("title"))
        if len(obj.content) > 50:
            return format_html("{}...", obj.content[:50])
        return obj.content

    def show_content(self, obj):
        from django.db.models import Avg
        result = TaskModel.objects.filter(id=obj.id).aggregate(Avg("content"))
        if len(obj.content) > 50:
            return format_html("{}...", obj.content[:50])
        return obj.content


admin.site.register(TaskModel, TaskAdmin)
