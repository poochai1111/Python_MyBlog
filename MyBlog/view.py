from django.shortcuts import render
from MyBlog.models import Blog
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import datetime


def default(request):
    return render(request, 'dashboard.html')


def login_blog(request):
    request.encoding = 'utf-8'
    if 'register' in request.GET:
        user_list = User.objects.all()
        return render(request, 'register.html', {"user_list": user_list})
    else:
        name = request.GET['name']
        pwd = request.GET['password']
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, 'MainBlog.html', {"name": name, "time": datetime.datetime.now()})
        else:
            return render(request, 'Error.html')


@csrf_exempt
def register_blog(request):
    if 'return' in request.POST:
        return render(request, 'dashboard.html')
    else:
        name = request.POST.get("name")
        pwd = request.POST.get("firstPwd")
        if User.objects.filter(username=name).count() > 0:
            return render(request, 'Register.html', {"error": "true"})
        else:
            User.objects.create_user(username=name, password=pwd, is_staff=1, is_active=1).save()
            if User.objects.filter(username=name).count() > 0:
                return render(request, 'dashboard.html')
            else:
                return render(request, 'Error.html')


@csrf_exempt
def create_blog(request):
    if 'submit' in request.POST:
        title = request.POST.get("blogTitle")
        content = request.POST.get("blogContent")
        user_id = request.user.id
        Blog(id=user_id, title=title, content=content, createdate=datetime.datetime.now(), updatedate=None).save()
        if Blog.objects.filter(id=user_id).count() > 0:
            return render(request, "success.html")
        else:
            return render(request, "Fail.html")


def change_password(request):
    return render(request, 'ChangePwd.html')


def account_display(request):
    return render(request, 'Account.html')
