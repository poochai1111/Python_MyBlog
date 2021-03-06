"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewsp
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import view
from TestModel.testdb import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.default, name="new_login"),
    path('login/', view.login_blog, name="login"),
    path('register/', view.register_blog),
    path('change/', view.change_password),
    path('account/', view.account_display, name="account"),
    path('create/', view.create_blog, name="blog"),
    path('delete/', view.blog_delete, name="delete"),
    path('edit/<int:blog_id>', view.edit_blog, name="edit"),
    path('test/', test),
    path('new_register/', view.new_register, name="new_register"),
    path('forgot_password/', view.new_password, name="new_password"),
    path('change_password/', view.change_password),
]
