from unicodedata import name
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.renderIndex, name='index'),
    path('renderLogin/', views.renderLogin, name='renderLogin'),
    path('renderLogin/login/', views.checklogin, name="login"),
    path('renderLogin/login/personal/', views.renderPersonal, name="personal"),
    # re_path(r'^renderLogin/[login/]*', views.checklogin, name="login"),
    path('index/login/', views.login, name="login"),
    # re_path(r'^index/login/', views.login, name="login"),
    path('renderLogin/signup/', views.renderSignup, name="signup"),
    path('renderLogin/signup/CT_signup/', views.CT_signup, name="CT_signup"),
    path('renderLogin/signup/KH_signup/', views.KH_signup, name="KH_signup"),
    path('renderLogin/signup/KH_signup/logout/', views.logout, name="logout"),
    path('renderLogin/signup/CT_signup/', views.logout, name="logout"),
    path('renderLogin/login/logout/', views.logout, name="logout"),
]