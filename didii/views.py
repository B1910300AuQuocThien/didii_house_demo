from multiprocessing import context
from re import template
from turtle import left
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import House, account
from django.urls import reverse
from django.contrib import messages
import sys
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# def index(request):
#     # template = loader.get_template('myfirst.html')
#     # return HttpResponse(template.render())
    
    
#     # myHouse = House.objects.all().values()
#     # output = ''
#     # for i in myHouse:
#     #     output += i['firstname'] + " "
#     # return HttpResponse(output)
    
    
#     myHouse = House.objects.all().values()
#     template = loader.get_template('index.html')
#     context = {
#         'myHouse': myHouse, 
#     }
#     return HttpResponse(template.render(context, request))

# def add(request):
#     template = loader.get_template('add.html')
#     return HttpResponse(template.render({}, request))

# def addHouse(request):
#     firs = request.POST['first']
#     last = request.POST['last']
#     house = House(firstname=firs, lastname=last)
#     house.save()
#     return HttpResponseRedirect(reverse('index'))

# def deleteHouse(request, id):
#     house = House.objects.get(id=id)
#     house.delete()
#     return HttpResponseRedirect(reverse('index'))

# def update(request, id):
#     house = House.objects.get(id=id)
#     template = loader.get_template('update.html')
#     context = {
#         'house': house,
#     }
#     return HttpResponse(template.render(context, request))

# def updateHouse(request, id):
#     fisrt = request.POST['first']
#     last = request.POST['last']
#     house = House.objects.get(id=id)
#     house.firstname = fisrt
#     house.lastname = last
#     house.save()
#     return HttpResponseRedirect(reverse('index'))

# def variable(request):
#     template = loader.get_template('variable.html')
#     house = House.objects.all().values()
#     context = {
#         'authname': 'thien',
#         'house': house,
#     }
#     return HttpResponse(template.render(context, request))

# def condition(request):
#     template = loader.get_template('condition.html')
#     context = {
#         'x': 1,
#     }
#     return HttpResponse(template.render(context, request))

# def forloop(request):
#     template = loader.get_template('forloop.html')
#     house = House.objects.all().values()
#     context = {
#         'house': house,
#     }
#     return HttpResponse(template.render(context, request))

# def cycle(request):
#     template = loader.get_template('cycle.html')
#     house = House.objects.all().values()
#     context = {
#         'house': house,
#     }
#     return HttpResponse(template.render(context, request))

# def goback(request):
#     return HttpResponseRedirect(reverse('index'))

# def mymaster(request):
#     template = loader.get_template('template.html')
#     house = House.objects.all().values()
#     context = {
#         'house': house,
#     }
#     return HttpResponse(template.render(context, request))

# def include(request):
#     template = loader.get_template('include.html')
#     return HttpResponse(template.render())

# def myfirst(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())


def renderIndex(request):
    return HttpResponse(loader.get_template('index.html').render())

def renderLogin(request):
    return HttpResponse(loader.get_template('login.html').render())

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    # left_side = loader.get_template('snippets/left_side.html')
    # template = loader.get_template('index.html')
    context = {
        'username': username,
    }
    # render(request, 'index.html', {'name': context})
    return HttpResponseRedirect(reverse('index', args=[context['username']]))
    
def logout(request):
    return HttpResponseRedirect(reverse('login'))