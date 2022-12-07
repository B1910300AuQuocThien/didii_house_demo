import email
from enum import unique
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from pkg_resources import to_filename

# Create your models here.
class account(models.Model): 
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=10)
    id_gr = models.ForeignKey('groupuser', on_delete=models.CASCADE)
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def get_id_gr(self):
        return self.id_gr
    
class groupuser(models.Model):  
    id_gr = models.CharField(max_length=10, primary_key=True, unique=True)
    name_gr = models.CharField(max_length=10)
    
    def get_id(self):
        return self.id_gr
class address(models.Model):
    id_add = models.CharField(max_length=10, primary_key=True)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    ward = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    
    def get_id(self):
        return self.id_add
    
    def get_address(self):
        return self.street + ", " + self.ward + ", " + self.district + ", " + self.city
    
class customer(models.Model):
    id_cus = models.AutoField(primary_key=True)
    name_cus = models.CharField(max_length=50)
    age = models.DateField()
    gender = models.BooleanField()
    # email = models.EmailField(max_length=250)
    email = models.ForeignKey(account, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    
    def get_id(self):
        return self.id_cus
    
    def get_name(self):
        return self.name_cus
    
    def get_age(self):
        return self.age
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_id_add(self):
        return self.id_add
    
class landlord(models.Model):
    id_landlord = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.DateField()
    gender = models.BooleanField()
    # email = models.EmailField()
    email = models.ForeignKey(account, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    numbranch = models.IntegerField()
    vote = models.FloatField()
    status = models.BooleanField()
    
    def get_id(self):
        return self.id_landlord
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_phone(self):
        return self.phone
    
    def get_count_branch(self):
        return self.numbranch
    
    def get_vote(self):
        return self.vote
    
    def get_status(self):
        return self.status
    
    def get_email(self):
        return self.email
    
    def get_id_add(self):
        return self.id_add
    
class branch(models.Model):
    id_landlord = models.ForeignKey(landlord, on_delete=models.CASCADE)
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    
    def get_id_landlord(self):
        return self.id_landlord

    def get_id_add(self):
        return self.id_add
    
class post(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_landlord = models.ForeignKey(landlord, on_delete=models.DO_NOTHING)
    date = models.DateField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/', default="")
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    id_interact = models.ForeignKey("interact", on_delete=models.CASCADE, to_field='id_interact')
    vote = models.FloatField()
    cost = models.FloatField()
    status = models.BooleanField()
    
    def get_id(self):
        return self.id_post
    
    def get_date(self):
        return self.date
    
    def get_title(self):
        return self.title
    
    def get_vote(self):
        return self.vote
    
    def get_cost(self):
        return self.cost
    
    def get_status(self):
        return self.status
    
    def get_id_add(self):
        return self.id_add
    
    def get_id_interact(self):
        return self.id_interact
    
class comment(models.Model):
    # id_cmt = models.AutoField(primary_key=True)
    # id_cmt = models.ForeignKey(post, on_delete=models.CASCADE)
    id_post = models.ForeignKey(post, on_delete=models.CASCADE)
    email = models.ForeignKey(customer, on_delete=models.CASCADE)
    date = models.DateField()
    cmt = models.CharField(max_length=250)
    
    def get_id(self):
        return self.id_cmt
    
    def get_date(self):
        return self.date
    
    def get_cmt(self):
        return self.cmt
class interact(models.Model):
    id_interact = models.CharField(max_length=10, primary_key=True)
    
    love_count = models.IntegerField()
    cmt_count = models.IntegerField()
    
    def get_id(self):
        return self.id_interact
    
    def get_love(self):
        return self.love_count
    
    def get_cmt_count(self):
        return self.cmt_count
    
class schedule(models.Model):
    id_schedule = models.CharField(max_length=10, primary_key=True)
    id_post = models.ForeignKey(post, on_delete=models.CASCADE, to_field="id_post")
    email_ll = models.ForeignKey(landlord, on_delete=models.CASCADE)
    email_cus = models.ForeignKey(customer, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    booking_date = models.DateField()
    
    def get_id(self):
        return self.id_schedule
    
    def get_appointment_date(self):
        return self.appointment_date
    
    def get_booking_date(self):
        return self.booking_date
