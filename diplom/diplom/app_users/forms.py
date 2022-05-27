from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileContractorModel, ProfileCustomerModel


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Логин')
    first_name = forms.CharField(max_length=30, required=True, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Фамилия')
    email = forms.EmailField(required=True, help_text='Email')
    profile_status = forms.CharField(max_length=2)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        help_texts = {
            'first_name': ('Имя'),
            'last_name': ('Фамилия'),
            'email': ('Email'),
        }


class ProfileContractorForm(forms.ModelForm):
    class Meta:
        model = ProfileContractorModel
        fields = ['city', 'phone', 'birth_day', 'university', 'faculty', 'specialization', 'profile_img']
        help_texts = {
            'city': ('Город'),
            'phone': ('Телефон'),
            'birth_day': ('День рождения'),
            'university': ('Институт'),
            'faculty': ('Факультет'),
            'specialization': ('Специализация'),
            'profile_img': ('Фотография'),
        }


class ProfileCustomerForm(forms.ModelForm):
    class Meta:
        model = ProfileCustomerModel
        fields = ['city', 'phone', 'company', 'profile_img']
        help_texts = {
            'city': ('Город'),
            'phone': ('Телефон'),
            'company': ('Компания'),
            'profile_img': ('Фотография'),
        }