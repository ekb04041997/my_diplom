from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks, name='tasks'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/info/', TaskDetailView.as_view(), name='task_detail'),
]