from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['pub_date', 'user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }
