from multiprocessing import context
from re import template
from tabnanny import check
from turtle import left
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import *
from django.urls import reverse
from django.contrib import messages
import sys
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def renderIndex(request):
    # return HttpResponse(loader.get_template('index.html').render())
    return render(request, 'index.html', {'url': "login/", 'text': "Đăng nhập"})

def renderLogin(request):
    return HttpResponse(loader.get_template('login.html').render())

def renderSignup(request):
    # return HttpResponse(loader.get_template("signup.html").render())
    return render(request, 'signup.html')

@csrf_exempt
def checklogin(request):
    username = request.POST['username']
    password = request.POST['password']
    acc = account.objects.all().values()
    # for i in range(0, acc.count()):
    #     print(acc[i]['id'])
    # print(username)
    context = {
        'username': username,
        
    }
    # print(context['username'])
    check = 0
    for i in range(0, acc.count()):
        if acc[i]['username'] == username and acc[i]['password'] == password:
            check = 1
            break
    if check == 0:
        # messages.error(request, "tai khoan không tôn tai")
        return HttpResponseRedirect("/didii/renderLogin/")
    return render(request, 'index.html', {'name': username, 'url': "logout/", 'text': "Đăng xuất"})
    
def login(request):
    return HttpResponseRedirect(reverse('renderLogin'))
    
def logout(request):
    return HttpResponseRedirect(reverse('renderLogin'))

def createPK(table_name, key):
    key = 'id_' + key
    table = table_name.objects.all().values()
    if table.count() == 0:
        # return key + str("_") + 1
        str_1 = (key, str(1))
        return "_".join(str_1)
    # print(key + "_" + (table.count + 1))
    str_2 = (key, str(table.count() + 1))
    return "_".join(str_2) 


@csrf_exempt
def CT_signup(request):
    CT_name = request.POST['CT_name']
    CT_age = request.POST['CT_age']
    CT_SDT = request.POST['CT_SDT']
    CT_gender = request.POST['CT_gender']
    CT_add_city = request.POST['CT_add_city']
    CT_add_district = request.POST['CT_add_district']
    CT_add_ward = request.POST['CT_add_ward']
    CT_add_street = request.POST['CT_add_street']
    CT_num_branch = request.POST['num_branch']
    CT_email = request.POST['CT_email']
    CT_pass = request.POST['CT_pass']
    
    acc = account.objects.filter(username = CT_email).order_by('id').first()
    print(acc)
    print(acc is None)
    
    if acc is not None:
        CT_acc = account(id = createPK(account, "acc"),
                         username = CT_email,
                         password = CT_pass)
        CT_acc.save()
        
        CT_add = address(id_add = createPK(address, "add"),
                         tinh_tp = CT_add_city,
                         quan_huyen = CT_add_district,
                         phuong_xa = CT_add_ward,
                         duong = CT_add_street)
        CT_add.save()
        
        CT_info = landlord(id_cus = CT_acc.id,
                           id_gr = "CT",
                           name_cus = CT_name,
                           age = CT_age,
                           gender = CT_gender,
                           email = CT_email,
                           phone = CT_SDT,
                           id_add = CT_add.id_add,
                           numbranch = CT_num_branch,
                           vote = '',
                           status = '')
        CT_info.save()
        return HttpResponse('index.html')
    else:
        return HttpResponseRedirect('/didii/renderLogin/signup/')
        