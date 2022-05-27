from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from .models import *
from .forms import *
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            profile_status = form.cleaned_data.get('profile_status')
            ProfileModel.objects.create(user=user, profile_status=profile_status)

            if form.cleaned_data.get('profile_status') == 'cu':
                company = request.POST.get('company')
                ProfileCustomerModel.objects.create(user=user, company=company)
                user_group = Group.objects.get(name='Customer')
                user.groups.add(user_group)

            else:
                ProfileContractorModel.objects.create(user=user)
                user_group = Group.objects.get(name='Contractor')
                user.groups.add(user_group)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('homepage')

    else:
        form = RegisterForm()

    return render(request, 'app_users/register.html', {'form': form})


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'app_homepage/homepage.html'


class CustomerDetailView(DetailView):
    model = User
    template_name = 'app_users/customer_detail.html'


class ContractorDetailView(DetailView):
    model = User
    template_name = 'app_users/contractor_detail.html'


class CreateContractorView(CreateView):
    model = ProfileContractorModel
    template_name = 'app_users/user_edit.html'


def edit_contractor_profile(request, pk):
    user = User.objects.get(id=pk)
    profile = ProfileContractorModel.objects.get(user=user)

    if request.method == 'POST':
        print(f'\n\n{request.POST}\n\n')
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileContractorForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            new_profile = profile_form.save()

        return redirect('contractor-detail', pk=pk)

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileContractorForm(instance=profile)

    return render(request, 'app_users/user_edit.html', {'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'user': user})


def edit_customer_profile(request, pk):
    user = User.objects.get(id=pk)
    profile = ProfileCustomerModel.objects.get(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileCustomerForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            new_profile = profile_form.save()

        return redirect('customer-detail', pk=pk)

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileCustomerForm(instance=profile)

    return render(request, 'app_users/user_edit.html', {'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'user': user})
