from django.shortcuts import render


def homepage(request):
    return render(request, 'app_homepage/homepage.html', context={'num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
