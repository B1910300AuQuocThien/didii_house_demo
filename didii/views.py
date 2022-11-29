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
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session


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



# Create your views here.

def renderIndex(request):
    # return HttpResponse(loader.get_template('index.html').render())
    
    return render(request, 'index.html', {'url': "login/", 'text': "Đăng nhập"})

def renderLogin(request):
    return HttpResponse(loader.get_template('login.html').render())

def renderSignup(request):
    return HttpResponse(loader.get_template("signup.html").render())
    # return render(request, 'signup.html')

def renderPersonal(request):
    request.session['edit_info'] = 'edit_info/'
    request.session['edit_profile'] = 'edit_profile/'
    request.session['create_post'] = 'create_post/'
    return render(request, 'personal.html')

@csrf_exempt
def checklogin(request):
    username = request.POST['username']
    password = request.POST['password']
    acc = account.objects.filter(username = username, password = password)
    if acc.first() is None:
        messages.error(request, "tai khoan khong ton tai")
        # url = render(request, "login.html")
        return HttpResponseRedirect(reverse('login'))
    else:
        print(acc.first().get_id_gr().get_id())
        if acc.first().get_id_gr().get_id() == "CT":
            user = landlord.objects.filter(email = username)
        else:
            user = customer.objects.filter(email = username)   
                
    request.session['name'] = user.first().get_name()
    request.session['email'] = user.first().get_email().get_username()
    request.session['address'] = user.first().get_id_add().get_address()
    request.session['url'] = "logout/"
    request.session['text'] = "Đăng xuất"
    loop = []
    for i in range(1, 6):
        loop.append(i)
    return render(request, 'index.html', {'url': 'logout/', 'text': "dang xuat", 'loop': loop})
    # return HttpResponseRedirect(reverse('index'))
    
def login(request):
    return HttpResponseRedirect(reverse('renderLogin'))
    
def logout(request):
    # Session.objects.all().delete()
    return HttpResponse(loader.get_template("login.html").render())

@csrf_exempt
def CT_signup(request):
    CT_name = request.POST['CT_name']
    CT_age = request.POST['CT_age']
    CT_phone = request.POST['CT_SDT']
    CT_gender = request.POST['CT_gender']
    CT_add_city = request.POST.getlist('CT_add_city')
    CT_add_district = request.POST.getlist('CT_add_district')
    CT_add_ward = request.POST.getlist('CT_add_ward')
    CT_add_street = request.POST.getlist('CT_add_street')
    CT_num_branch = request.POST['num_branch']
    CT_email = request.POST['CT_email']
    CT_pass = request.POST['CT_pass']
    
    # print(CT_add_city[0)
    # return HttpResponse("index.html")
    acc = account.objects.filter(username = CT_email).first()
    
    CT_age = CT_age.split(" / ")
    CT_age = list(reversed(CT_age))
    CT_age = "-".join(CT_age)

    if acc is None:
        CT_acc = account(username = CT_email,
                         password = CT_pass,
                         id_gr = groupuser.objects.get(id_gr = 'CT'))
        CT_acc.save()
        
        CT_add = address(id_add = createPK(address, "add"),
                         tinh_tp = CT_add_city[0],
                         quan_huyen = CT_add_district[0],
                         phuong_xa = CT_add_ward[0],
                         duong = CT_add_street[0])
        CT_add.save()
        # print(CT_add)
        
        CT_info = landlord(name = CT_name,
                           age = CT_age,
                           gender = CT_gender,
                           email = account.objects.get(username = CT_email),
                           phone = CT_phone,
                           id_add = address.objects.get(id_add = CT_add.get_id()),
                           numbranch = CT_num_branch,
                           vote = 5,
                           status = True)
        CT_info.save()
        
        if CT_num_branch != 0:
           for i in range(0, int(CT_num_branch)):
               CT_add_branch = address(id_add = createPK(address, "add"),
                                       tinh_tp = CT_add_city[i + 1],
                                       quan_huyen = CT_add_district[i + 1],
                                       phuong_xa = CT_add_ward[i + 1],
                                       duong = CT_add_street[i + 1])
               CT_add_branch.save() 
               branch_info = branch(id_landlord = landlord.objects.get(id_landlord = CT_info.get_id()),
                                    id_add = address.objects.get(id_add = CT_add_branch.get_id()))
               branch_info.save()
        
        request.session['name'] = CT_name
        return render(request, "index.html", {'url': "logout/", 'text': "Đăng xuất"})
    else:
        return HttpResponseRedirect('/didii/renderLogin/signup/')
        
        
@csrf_exempt
def KH_signup(request):
    print(request.POST)
    KH_name = request.POST['KH_name']
    KH_age = request.POST['KH_age']
    KH_phone = request.POST['KH_SDT']
    KH_gender = request.POST['KH_gender']
    print(KH_gender)
    KH_add_city = request.POST['KH_add_city']
    KH_add_district = request.POST['KH_add_district']
    KH_add_ward = request.POST['KH_add_ward']
    KH_add_street = request.POST['KH_add_street']
    KH_email = request.POST['KH_email']
    KH_pass = request.POST['KH_pass']
    
    acc = account.objects.filter(username = KH_email).first()
    
    KH_age = KH_age.split(" / ")
    KH_age = list(reversed(KH_age))
    KH_age = "-".join(KH_age)
    
    if acc is None:
        KH_acc = account(username = KH_email,
                         password = KH_pass,
                         id_gr =  groupuser.objects.get(id_gr = "KH"))
        KH_acc.save()
        
        KH_add = address(id_add = createPK(address, "add"),
                         tinh_tp = KH_add_city,
                         quan_huyen = KH_add_district,
                         phuong_xa = KH_add_ward,
                         duong = KH_add_street)
        KH_add.save()
    
        KH_info = customer(name_cus = KH_name,
                           age = KH_age,
                           gender = KH_gender,
                           email = account.objects.get(username = KH_email),
                           phone = KH_phone,
                           id_add = address.objects.get(id_add = KH_add.get_id()))
        KH_info.save()
        request.session['name'] = KH_name
        request.session['email'] = KH_info.get_email().get_username()
        request.session['address'] = KH_info.get_id_add().get_address()
        return render(request, "index.html", {'url': "logout/", 'text': "Đăng xuất"})
    else:
        request.session['error'] = "email da tồn tại"
        # return HttpResponseRedirect('/didii/renderLogin/signup/')
        return HttpResponse("signup.html")


def edit(request, action):
    request.session[action] = '#'
    return render(request, 'personal.html', {'action': action})
