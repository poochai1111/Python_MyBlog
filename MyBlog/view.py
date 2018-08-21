from django.shortcuts import render, render_to_response
from MyBlog.models import User, Blog
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
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
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            if User.objects.filter(name=name, password=pwd).count() > 0:
                return render(request, 'MainBlog.html', {"name": name, "time": datetime.datetime.now()})
            else:
                return render(request, 'Error.html')
        else:
            return render(request, 'Error.html')


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


@csrf_exempt
def blog(request):
    if 'submit' in request.POST:
        title = request.POST.get("blogTitle")
        content = request.POST.get("blogContent")

        user_name = request.user.name
        user_id = User.objects.filter(name=user_name).get(id)
        Blog(id=user_id, title=title, content=content, createdate=datetime.datetime.now(), updatedate=None).save()
        if Blog.objects.filter(id=user_id).count() > 0:
            return render_to_response("success.html")
        else:
            return render_to_response("Fail.html")


def change(request):
    return render_to_response('ChangePwd.html')


def account(request):
    return render_to_response('Account.html')
