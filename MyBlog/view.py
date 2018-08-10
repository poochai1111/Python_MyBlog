from django.shortcuts import render, render_to_response
from MyBlog.util import dbUtil


def default(request):
    return render(request, 'dashboard.html')


def login(request):
    request.encoding = 'utf-8'
    dic = {}
    name = request.GET['name'].encode('utf-8')
    if name is None or len(name) < 2:
        return render_to_response('register.html')
    else:
        name = request.GET['name'].encode('utf-8')
        pwd = request.GET['password'].encode('utf-8')
        dic["name"] = name
        dic["password"] = pwd
        if dbUtil.select(dic):
            return render_to_response('MainBlog.html')
        else:
            return render_to_response('Error.html')


def register(request):
    request.encoding = 'utf-8'
    dic = {}
    name = request.GET['name'].encode('utf-8')
    if name is not None or len(name) < 2:
        return render_to_response('dashboard.html')
    else:
        name = request.GET['name']
        pwd = request.GET['password']
        dic["name"] = name
        dic["password"] = pwd
        if dbUtil.insert(dic):
            return render_to_response('dashboard.html')
        else:
            return render_to_response('Error.html')

