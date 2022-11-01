import email
from enum import unique
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from pkg_resources import to_filename

# Create your models here.
class account(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    
    def get_id_acc(self):
        return self.id
    
class groupuser(models.Model):
    id_gr = models.CharField(max_length=10, primary_key=True)
    name_gr = models.CharField(max_length=10)

class address(models.Model):
    id_add = models.CharField(max_length=10, primary_key=True)
    tinh_tp = models.CharField(max_length=20)
    quan_huyen = models.CharField(max_length=20)
    phuong_xa = models.CharField(max_length=20)
    duong = models.CharField(max_length=20)
    
    def get_id_add(self):
        return self.id_add
    
    def get_address(self):
        return self.duong + ", " + self.phuong_xa + ", " + self.quan_huyen + ", " + self.tinh_tp
    
class customer(models.Model):
    id_cus = models.ForeignKey(account, on_delete=models.CASCADE, to_field='id')
    id_gr = models.ForeignKey(groupuser, on_delete=models.CASCADE, to_field='id_gr')
    name_cus = models.CharField(max_length=50)
    age = models.DateField()
    gender = models.BooleanField()
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10)
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    
    def get_id_cus(self):
        return self.id_cus
    
class landlord(models.Model):
    id_landlord = models.CharField(max_length=10, primary_key=True)
    id_gr = models.ForeignKey(groupuser, on_delete=models.CASCADE, to_field='id_gr')
    name = models.CharField(max_length=50)
    age = models.DateField()
    gender = models.BooleanField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    numbranch = models.IntegerField()
    vote = models.FloatField()
    status = models.BooleanField()
    
    def get_id_ll(self):
        return self.id_landlord
    
class branch(models.Model):
    id_landlord = models.ForeignKey(landlord, on_delete=models.CASCADE, to_field='id_landlord')
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    
class post(models.Model):
    id_post = models.CharField(max_length=10, primary_key=True)
    id_landlord = models.ForeignKey(landlord, on_delete=models.CASCADE, to_field='id_landlord')
    date = models.DateField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    # img
    id_add = models.ForeignKey(address, on_delete=models.CASCADE, to_field='id_add')
    id_interact_count = models.ForeignKey("interact", on_delete=models.CASCADE, to_field='id_interact')
    id_cmt = models.ForeignKey("comment", on_delete=models.CASCADE, to_field='id_cmt')
    vote = models.FloatField()
    cost = models.FloatField()
    status = models.BooleanField()
    
class comment(models.Model):
    id_cmt = models.CharField(max_length=10, primary_key=True)
    id_post = models.ForeignKey(post, on_delete=models.CASCADE, to_field='id_post')
    id = models.ForeignKey(account, on_delete=models.CASCADE, to_field='id')
    date = models.DateField()
    cmt = models.CharField(max_length=250)
    
class interact(models.Model):
    id_interact = models.CharField(max_length=10, primary_key=True)
    love_count = models.IntegerField()
    cmt_count = models.IntegerField()
    
class schedule(models.Model):
    id_schedule = models.CharField(max_length=10, primary_key=True)
    id_landlord = models.ForeignKey(landlord, on_delete=models.CASCADE, to_field='id_landlord')
    id_post = models.ForeignKey(post, on_delete=models.CASCADE, to_field="id_post")
    id_cus = models.ForeignKey(account, on_delete=models.CASCADE, to_field='id')
    appointment_date = models.DateField()
    booking_date = models.DateField()
    