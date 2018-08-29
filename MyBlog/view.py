from django.shortcuts import render
from MyBlog.models import MyBlog
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import datetime
from django.core import serializers


def default(request):
    return render(request, 'dashboard.html')


def login_blog(request):
    request.encoding = 'utf-8'
    if 'register' in request.GET:
        user_list = User.objects.all()
        return render(request, 'register.html', {"user_list": user_list})
    elif 'submit' in request.GET:
        name = request.GET['name']
        pwd = request.GET['password']
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            title = "Welcome " + name + ", Login time:" + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            return render(request, 'MainBlog.html', {"welcome": title})
        else:
            return render(request, 'Error.html')
    else:
        return render(request, 'dashboard.html')


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
        if request.POST.get("blog_id") == 'undefined':
            blog_id = None
        else:
            blog_id = int(request.POST.get("blog_id"))
        user_name = request.user.username
        if blog_id is not None:
            MyBlog.objects.filter(id=blog_id).update(title=title, content=content)
            if MyBlog.objects.filter(id=blog_id).values("update_date") is not None:
                return render(request, "success.html", {"title": "Update blog success"})
            else:
                return render(request, "Fail.html", {"title": "Update Blog Failed!!!"})
        else:
            MyBlog(name=user_name, title=title, content=content, create_date=datetime.datetime.now(),
                   update_date=None).save()
            if MyBlog.objects.filter(name=user_name, title=title).count() > 0:
                return render(request, "success.html", {"title": "Create blog success"})
            else:
                return render(request, "Fail.html", {"title": "Create Blog Failed!!!"})
    else:
        title = "Welcome " + request.user.username + ", Login time:" + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        return render(request, "MainBlog.html", {"welcome": title})


def edit_blog(request, blog_id):
    user_name = request.user.username
    blog = list(MyBlog.objects.filter(id=blog_id).values())
    title = "Welcome " + user_name + ", Update blog time:" + datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    return render(request, 'MainBlog.html', {"blog_info": blog, "welcome": title})


def change_password(request):
    return render(request, 'ChangePwd.html')


def account_display(request):
    user_name = request.user.username
    blog = list(MyBlog.objects.filter(name=user_name))
    user = list(User.objects.filter(username=user_name))
    paginator = Paginator(blog, 10)
    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    return render(request, 'Account.html', {"blog_info": blog, "blog_count": len(blog), "user_info": user})


@csrf_exempt
def blog_delete(request):
    blog_id_list = request.POST["blog_id"]
    if "," in blog_id_list:
        array = blog_id_list.split(",")
        for blog_id in array:
            MyBlog.objects.filter(id=blog_id).delete()
    else:
        MyBlog.objects.filter(id=blog_id_list).delete()
    user_name = request.user.username
    blog = serializers.serialize('json', MyBlog.objects.filter(name=user_name))
    return JsonResponse(blog, content_type="application/json", safe=False)
