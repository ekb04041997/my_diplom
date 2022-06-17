from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks, name='tasks'),
    path('customer/user=<int:user_id>', customer_tasks, name='customer_tasks'),
    path('contractor/user=<int:user_id>', contractor_tasks, name='contractor_tasks'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/info/', TaskDetailView.as_view(), name='task_detail'),
    path('tag_detail/<int:pk>/', tag_detail, name='tag_detail'),
    path('customer/user=<int:user_id>/tag_detail/<int:pk>/', customer_tag_detail, name='customer_tag_detail'),
    path('contractor/user=<int:user_id>/tag_detail/<int:pk>/', contractor_tag_detail, name='contractor_tag_detail'),
    path('user=<int:user_id>/contractor_chat/', contractor_chat, name='contractor_chat'),
    path('user=<int:user_id>/customer_chat/', customer_chat, name='customer_chat'),
    path('add_contractor_task/<int:user_id>/<int:task_id>', add_contractor_task, name='add_contractor_task'),
]