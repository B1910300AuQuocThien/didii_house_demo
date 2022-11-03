from multiprocessing import context
from re import template
from tabnanny import check
from turtle import left
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import account, address, customer
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
    return HttpResponse(loader.get_template("signup.html").render())

def renderCreateAcc(request):
    return HttpResponse(loader.get_template('create_account.html').render())


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
    
    acc = account.objects.filter(username = CT_email).values()
    
    # print(type(acc))
    if acc is not None:
        return HttpResponseRedirect("/didii/renderLogin/signup/")
    
    KH_acc = account(id = createPK(account, "acc"),
                     username = CT_email,
                     password = CT_pass
                     )
    KH_acc.save()
    # KH_info = customer(id_cus = createPK(customer, "cus"),
    #                    )
    
    KH_add = address(id_add = createPK(address, "add"),
                      tinh_tp = CT_add_city,
                      quan_huyen = CT_add_district,
                      phuong_xa = CT_add_ward,
                      duong = CT_add_street)
    KH_add.save()
    # print(CT_age)
    return render(request, 'index.html')