from django.shortcuts import render, render_to_response
from MyBlog.models import User
from django.views.decorators.csrf import csrf_exempt
import datetime


def default(request):
    return render(request, 'dashboard.html')


def login(request):
    request.encoding = 'utf-8'
    if 'register' in request.GET:
        return render_to_response('register.html')
    else:
        name = request.GET['name']
        pwd = request.GET['password']
        if User.objects.filter(name=name, password=pwd).count() > 0:
            return render_to_response('MainBlog.html')
        else:
            return render_to_response('Error.html')

@csrf_exempt
def register(request):
    if 'return' in request.POST:
        return render_to_response('dashboard.html')
    else:
        name = request.POST.get("name")
        pwd = request.POST.get("firstPwd")
        User(name=name, password=pwd, createdate=datetime.datetime.now(), updatedate=None, status=0).save()
        if User.objects.filter(name=name, password=pwd).count() > 0:
            return render_to_response('dashboard.html')
        else:
            return render_to_response('Error.html')


def change(request):
    return render_to_response('ChangePwd.html')


def account(request):
    return render_to_response('Account.html')
