from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *


admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = ProfileModel


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]
    list_display = ['username', 'id', 'first_name', 'last_name', 'email']

class ProfileCustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'id']

class ProfileContractorAdmin(admin.ModelAdmin):
    list_display = ['user', 'id']


admin.site.register(User, UserProfileAdmin)
admin.site.register(ProfileCustomerModel, ProfileCustomerAdmin)
admin.site.register(ProfileContractorModel, ProfileContractorAdmin)

