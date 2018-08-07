from django.shortcuts import render


def default(request):
    return render(request, 'dashboard.html')


def register(request):
    return render(request, 'register.html')
