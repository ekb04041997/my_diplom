from django.urls import path
from .views import *


urlpatterns = [
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('contractor/<int:pk>/info/', ContractorDetailView.as_view(), name='contractor-detail'),
    path('customer/<int:pk>/info/', CustomerDetailView.as_view(), name='customer-detail'),
    path('contractor/<int:pk>/edit/', edit_contractor_profile, name='contractor-edit'),
    path('customer/<int:pk>/edit/', edit_customer_profile, name='customer-edit'),
]
