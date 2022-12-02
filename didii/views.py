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
    # return render(request, 'signup.html')gettinh


def renderPersonal(request):
    request.session['edit_info'] = 'edit_info/'
    request.session['edit_profile'] = 'edit_profile/'
    request.session['create_post'] = 'create_post/'
    return render(request, 'personal.html')


@csrf_exempt
def checklogin(request):
    username = request.POST['username']
    password = request.POST['password']
    acc = account.objects.filter(username=username, password=password)
    if acc.first() is None:
        messages.error(request, "tai khoan khong ton tai")
        # url = render(request, "login.html")
        return HttpResponseRedirect(reverse('login'))
    else:
        print(acc.first().get_id_gr().get_id())
        if acc.first().get_id_gr().get_id() == "CT":
            user = landlord.objects.filter(email=username)
        else:
            user = customer.objects.filter(email=username)

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
def signup(request):
    name = request.POST['name']
    age = request.POST['age']
    phone = request.POST['num_phone']
    gender = request.POST['gender']
    typeuser = request.POST['groupuser']
    add_city = request.POST.getlist('city')
    add_district = request.POST.getlist('district')
    add_ward = request.POST.getlist('ward')
    add_street = request.POST.getlist('street')
    num_branch = request.POST['num_branch']
    email = request.POST['email']
    upass = request.POST.get('password')
    # print(upass)
    # print(add_city[0)
    # return HttpResponse("index.html")
    acc = account.objects.filter(username=email).first()

    age = age.split(" / ")
    age = list(reversed(age))
    age = "-".join(age)

    if typeuser == 'KH' and acc is None:

        acc = account(username=email,
                      password=upass,
                      id_gr=groupuser.objects.get(id_gr=typeuser))
        acc.save()

        add = address(id_add=createPK(address, "add"),
                      city=add_city[0],
                      district=add_district[0],
                      ward=add_ward[0],
                      street=add_street[0])
        add.save()

        info = customer(name_cus=name,
                        age=age,
                        gender=gender,
                        email=account.objects.get(username=email),
                        phone=phone,
                        id_add=address.objects.get(id_add=add.get_id()))
                    
        info.save()
        request.session['name'] = name
        return render(request, "index.html", {'url': "logout/", 'text': "Đăng xuất"})
    
    elif typeuser == 'CT' and acc is None:
        acc = account(username=email,
                      password=upass,
                      id_gr=groupuser.objects.get(id_gr=typeuser))
        acc.save()

        add = address(id_add=createPK(address, "add"),
                      city=add_city[0],
                      district=add_district[0],
                      ward=add_ward[0],
                      street=add_street[0])
        add.save()
        # print(add)

        info = landlord(name=name,
                        age=age,
                        gender=gender,
                        email=account.objects.get(username=email),
                        phone=phone,
                        id_add=address.objects.get(id_add=add.get_id()),
                        numbranch=num_branch,
                        vote=5,
                        status=True)
        info.save()

        if num_branch != 0:
            for i in range(0, int(num_branch)):
                add_branch = address(id_add=createPK(address, "add"),
                                     city=add_city[i + 1],
                                     district=add_district[i + 1],
                                     ward=add_ward[i + 1],
                                     street=add_street[i + 1])
                add_branch.save()
                branch_info = branch(id_landlord=landlord.objects.get(id_landlord=info.get_id()),
                                     id_add=address.objects.get(id_add=add_branch.get_id()))
                branch_info.save()

        request.session['name'] = name
        request.session['email'] = email
        return render(request, "index.html", {'url': "logout/", 'text': "Đăng xuất"})
    else:
        return HttpResponseRedirect('/didii/renderLogin/signup/')


def edit(request, action):
    request.session[action] = '#'
    if action == 'create_post':
        id_add_branch = []
        add_branch_detail = []
        
        user = landlord.objects.get(email = account.objects.get(username = request.session['email']))
        branchs = branch.objects.filter(id_landlord = user.id_landlord)
        
        # print(branchs[0].get_id_add().get_id())
        for branch_detail in branchs:
            add_branch = address.objects.get(id_add = branch_detail.get_id_add().get_id())
            id_add_branch.append(add_branch.id_add)
            add_branch_detail.append(add_branch.get_address())
            
        context = {
            'id': id_add_branch,
            'add': add_branch_detail
        }
    return render(request, 'personal.html', {'action': action, 'context': context})

def cancel(request, action):
    return HttpResponseRedirect(reverse('personal'))    
    # return HttpResponse(loader.get_template('personal.html').render())


@csrf_exempt
def updata_info(request):
    age = request.POST['age']
    age = age.split(" / ")
    age = list(reversed(age))
    age = "-".join(age)
    
    acc = account.objects.get(username = request.session['email'])
    # print(acc.get_id_gr() == groupuser.objects.get(id_gr = 'KH'))
    if acc.get_id_gr() == groupuser.objects.get(id_gr = 'KH'):
        user = customer.objects.get(email = request.session['email'])
        user.name_cus = request.POST['name']
        user.age = age
        user.gender = request.POST['gender']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        
        add = address.objects.get(id_add = user.get_id_add())
        add.city = request.POST.getlist('city')[0]
        add.district = request.POST.getlist('district')[0]
        add.ward = request.POST.getlist('ward')[0]
        add.street = request.POST.getlist('street')[0]
    else:
        user = landlord.objects.get(email = request.session['email'])
        user.name = request.POST['name']
        user.age = age
        user.gender = request.POST['gender']
        user.phone = request.POST['num_phone']
        user.numbranch = request.POST['num_branch']
        # print(user.get_id_add().get_id())
        add = address.objects.get(id_add = user.get_id_add().get_id())
        add.city = request.POST.getlist('city')[0]
        add.district = request.POST.getlist('district')[0]
        add.ward = request.POST.getlist('ward')[0]
        add.street = request.POST.getlist('street')[0]
       
        add.save()
        user.save()
        # print(request.POST['num_branch'] != 0)
        if int(request.POST['num_branch']) != 0:
            old_branch = branch.objects.filter(id_landlord = user.id_landlord)
            # print(old_branch is not None)
            
            if old_branch is not None:
                old_branch.delete()
            
            for i in range(0, int(request.POST['num_branch'])):
                add_branch = address(id_add = createPK(address, "add"),
                                    city = request.POST.getlist('city')[i + 1],
                                    district = request.POST.getlist('district')[i + 1],
                                    ward = request.POST.getlist('ward')[i + 1],
                                    street = request.POST.getlist('street')[i + 1])
                add_branch.save()
                branch_info = branch(id_landlord=landlord.objects.get(id_landlord = user.get_id()),
                                    id_add=address.objects.get(id_add = add_branch.get_id()))
                branch_info.save()

    return HttpResponseRedirect(reverse('personal'))
        
        
@csrf_exempt
def update_post(request):
    post_title = request.GET['post_title']
    post_content = request.GET['post_content']
    post_img = request.GET['post_img']
    post_cost = request.GET['post_cost']
    
    post_detail = post(id_landlord = landlord.objects.get(email = request.session['email']),
                       date = '',
                       title = post_title,
                       content = post_content,
                       img = post_img,
                       id_add = '')
    
    context = {
        'post': post_detail
    }
    print(request.GET)
    return HttpResponse('ngan')