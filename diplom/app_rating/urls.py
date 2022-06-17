from django.urls import path
from .views import *

urlpatterns = [
    path('', rating_all, name='rating'),
    path('tag_detail/<int:pk>/', rating_for_category, name='category_detail'),
]
