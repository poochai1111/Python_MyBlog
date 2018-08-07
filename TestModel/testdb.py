# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import User

import datetime


def test(request):

    response1 = ""

    # Get all data
    list = User.objects.all()

    # Update Table
    # test1 = User.objects.get(id=2)
    # test1.name = 'aaa'
    # test1.save()
    User.objects.filter(id=2).update(name='Aaa')

    # Delete Data
    User.objects.filter(id=4).delete()

    # Insert data
    test1 = User(id='004', name='CCC', password='123456', createdate=datetime.datetime.now(), updatedate=datetime.datetime.now(), status=1)
    test1.save()

    # Loop all data
    for var in list:
        response1 += var.name + " "

    return HttpResponse("<p>" + response1 + "</p>")
