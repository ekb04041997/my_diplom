from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks, name='tasks'),
    path('user=<int:user_id>', user_tasks, name='user_tasks'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/info/', TaskDetailView.as_view(), name='task_detail'),
    path('tag_detail/<int:pk>/', tag_detail, name='tag_detail'),
    path('user=<int:user_id>/tag_detail/<int:pk>/', user_tag_detail, name='user_tag_detail'),
]