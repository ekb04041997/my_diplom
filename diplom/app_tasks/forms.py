from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['pub_date', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title_field'}),
        }


class CustomerCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['pub_date', 'user', 'file', 'task']


class ContractorCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['pub_date', 'user', 'task']


class ContractorTaskForm(forms.Form):
    class Meta:
        model = ContractorTask
        exclude = ['pub_date', 'user', 'task']
