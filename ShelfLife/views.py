from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def index(response):
    return render(response, 'ShelfLife/index.html', { 'all': User.objects.all(),
                                                      'thing': Thing.objects.all(),
                                                      })


def detail(response, usr):
    l = []
    man = User.objects.get(pk = usr)
    for i in UserConnections.objects.all():
        if i.usr == man:
            l.append(i)
    return render(response, 'ShelfLife/detail.html', { 'Connections': l, 'name':man.name, 'id':man.pk})


def add(response):
    return render(response, 'ShelfLife/form.html')


def save(response):
    name = response.POST['names']
    image = response.POST['image']
    New_User = User()
    New_User.name = name
    New_User.image = image
    New_User.save()
    return redirect('index')


def makeConnections(response, usr):
    string = response.POST['like']
    data = string.split()
    for i in data:
        temp = UserConnections()
        temp.usr = User.objects.get(pk = usr)
        obj = Thing()
        obj.name = i
        obj.save()
        temp.thing = obj
        temp.save()
    return redirect('details', usr = usr)


def delete(response, usr):
    obj = get_object_or_404(User, pk = usr)
    obj.delete()
    return redirect('index')


def tdelete(response, thing):
    obj = get_object_or_404(Thing, pk=thing)
    obj.delete()
    return redirect('index')
