from multiprocessing import context
from re import template
from tabnanny import check
from turtle import left
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from datetime import date
from django.shortcuts import redirect, render
from django.core import serializers

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
    posts = post.objects.all()
    sessions = Session.objects.all().first()
    calendars = ''
    if sessions is not None:
        if request.session['id_gr'] == 'CT':
            print(request.session['email'])
            calendars = schedule.objects.filter(email_ll = landlord.objects.get(email = request.session['email']))
        
        if request.session['id_gr'] == 'KH':
            calendars = schedule.objects.filter(email_cus = customer.objects.get(email = request.session['email']))
        
        return render(request, 'index.html', {'url': 'logout/', 'text': "Đăng xuất", 'posts': posts, 'calendars': calendars})
    if sessions is None:
        return render(request, 'index.html', {'url': 'login/', 'text': "Đăng nhập", 'posts': posts})


def renderSignup(request):
    return HttpResponse(loader.get_template("signup.html").render())


def renderPersonal(request):
    user = account.objects.get(username = request.session['email'])
    posts = ''
    if request.session['id_gr'] == 'CT':
        print(request.session['email'])
        calendars = schedule.objects.filter(email_ll = landlord.objects.get(email = request.session['email']))
        posts = post.objects.filter(id_landlord = landlord.objects.get(email = request.session['email']))

    if request.session['id_gr'] == 'KH':
        calendars = schedule.objects.filter(email_cus = customer.objects.get(email = request.session['email']))
        
    
    if user.get_id_gr().get_id() == 'CT':
        user = landlord.objects.get(email = user.username)
    else:
        user.get_id_gr().get_id() == 'KH'
        user = customer.objects.get(email = user.username)
    
    
    request.session['name'] = user.get_name()
    request.session['email'] = user.get_email().get_username()
    request.session['address'] = user.get_id_add().get_address()
    request.session['edit_info'] = 'edit_info/'
    request.session['edit_profile'] = 'edit_profile/'
    request.session['create_post'] = 'create_post/'
    print(posts)
    return render(request, 'personal.html', {'calendars': calendars, 'posts': posts})


@csrf_exempt
def schedules(request, id):
    if Session.objects.all().first() is not None :
        
        if request.session['id_gr'] == 'CT':
            messages.error(request, "chỉ khách hàng mới có thể đặt lịch")
            return render(request, 'snippets/schedule.html')
        
        if request.method == 'POST':
            if schedule.objects.filter(email_cus = customer.objects.get(email = request.session['email']),
                                       id_post = id):
                messages.error(request, "bạn đã đặt lịch trước đó")
                return render(request, 'snippets/schedule.html')
            else:
                appointment = request.POST['age']
                appointment = appointment.split(" / ")
                appointment = list(reversed(appointment))
                appointment = "-".join(appointment)
                
                posts = post.objects.get(id_post = id)
                email_ll = posts.id_landlord
                
                book_date = date.today()
                book_date = str(book_date).split('-')
                book_date = '-'.join(book_date)
                
                calendar = schedule(id_schedule = createPK(schedule, "sche"),
                                    id_post = post.objects.get(id_post = id),
                                    email_ll = email_ll,
                                    email_cus = customer.objects.get(email = request.session['email']),
                                    appointment_date = appointment,
                                    booking_date = book_date)

                calendar.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/')
        else:
            return render(request, 'snippets/schedule.html')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/login/')
        
    
@csrf_exempt
def checklogin(request, *args):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        acc = account.objects.filter(username=username, password=password)
        if acc.first() is None:
            messages.error(request, "tai khoan khong ton tai")
            # url = render(request, "login.html")
            return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/login/')
        else:
            print(acc.first().get_id_gr().get_id())
            if acc.first().get_id_gr().get_id() == "CT":
                user = landlord.objects.filter(email=username)
            else:
                user = customer.objects.filter(email=username)
        
        request.session['id_gr'] = acc.first().get_id_gr().get_id()
        request.session['name'] = user.first().get_name()
        request.session['email'] = user.first().get_email().get_username()
        request.session['address'] = user.first().get_id_add().get_address()
        request.session['url'] = "logout/"
        request.session['text'] = "Đăng xuất"
        return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/')
    else:
        return render(request, 'login.html')
    

def logout(request):
    Session.objects.all().delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/login/')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
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
            request.session['id_gr'] = 'KH'
            request.session['email'] = email
            request.session['name'] = name
            return HttpResponseRedirect(reverse(renderIndex))
        
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
            request.session['id_gr'] = 'CT'
            request.session['name'] = name
            request.session['email'] = email
            return HttpResponseRedirect(reverse(renderIndex))
        else:
            messages.error(request, 'email đã tồn tại')
            return HttpResponseRedirect(reverse(signup))
    else:
        return render(request, 'signup.html')
    

def edit(request, action):
    request.session[action] = ''
    add = ''
    id = ''
    if action == 'create_post' and request.session['id_gr'] == 'CT':
        id = branch.objects.filter(id_landlord = landlord.objects.get(email = request.session['email']))
        add = []
        for i in id:
            add.append(i.get_id_add().get_address())
        return render(request, 'personal.html', {'action': action, 'ids':id, 'adds': add})
    if action == 'edit_info':
        return render(request, 'personal.html', {'action': action, 'ids':id, 'adds': add})
    
    return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/personal/')


def cancel(request, action):
    print(type(request.META.get('HTTP_REFERER')))
    return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/personal/')    


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

    # return HttpResponseRedirect(reverse('personal'))
    return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/login/personal/')    
    
        
@csrf_exempt
def update_post(request):
    if request.session['id_gr'] == 'CT':
        post_title = request.POST['post_title']
        post_content = request.POST['post_content']
        post_img = request.FILES['post_img']
        post_cost = request.POST['post_cost']
        post_add = request.POST.get('post_id_add')
        post_date = date.today()
        post_date = str(post_date).split('-')
        post_date = '-'.join(post_date)
        
        if post_add is None:
            post_add = landlord.objects.get(email = request.session['email']).get_id_add().get_id()
        
        feel = interact(id_interact = createPK(interact, 'inter'), 
                        love_count = 0,
                        cmt_count = 0)
        feel.save()
        post_detail = post(id_landlord = landlord.objects.get(email = request.session['email']),
                        date = post_date,
                        title = post_title,
                        content = post_content,
                        img = post_img,
                        id_add = address.objects.get(id_add = post_add),
                        id_interact = interact.objects.get(id_interact = feel.get_id()),
                        vote = 0,
                        cost = post_cost,
                        status = True)
        post_detail.save()
        messages.success(request, "đăng bài thành công")
        return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/personal/')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/personal/')
    

def heart(request, id):
    if Session.objects.all().first() is not None:
        id = post.objects.get(id_post = id)
        heart = interact.objects.get(id_interact = id.get_id_interact().get_id())
        heart.love_count += 1
        heart.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/didii/index/login/')
   

def back(request, id):
    if Session.objects.all().first() is not None:
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse(checklogin))
        
def delete_post(request, id):
    del_post = post.objects.get(id_post = id)
    del_post.delete()
    messages.success(request, "xóa thành công")
    return HttpResponseRedirect(reverse(renderPersonal  ))