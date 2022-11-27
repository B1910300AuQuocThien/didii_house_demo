from unicodedata import name
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.renderIndex, name='index'),
    path('renderLogin/', views.renderLogin, name='renderLogin'),
    # re_path('[login/]$', views.checklogin, name="login"),
    path('renderLogin/login/', views.checklogin, name="login"),
    path('renderLogin/login/personal/', views.renderPersonal, name="personal"),
    re_path(r'renderLogin/login/personal/(?P<action>edit_info|edit_profile|create_post)/$', views.edit, name='edit'),
    re_path(r'^renderLogin/\w/[login]*/login/$', views.checklogin, name="login"),
    path('index/login/', views.login, name="login"),
    # re_path(r'^index/login/', views.login, name="login"),
    path('renderLogin/signup/', views.renderSignup, name="signup"),
    path('renderLogin/signup/CT_signup/', views.CT_signup, name="CT_signup"),
    path('renderLogin/signup/CT_signup/personal/', views.renderPersonal, name="personal"),
    
    path('renderLogin/signup/KH_signup/', views.KH_signup, name="KH_signup"),
    path('renderLogin/signup/KH_signup/personal/', views.renderPersonal, name="personal"),
    re_path(r'renderLogin/signup/KH_signup/personal/(?P<action>edit_info|edit_profile|create_post)/$', views.edit, name="edit"),
    
    path('renderLogin/signup/KH_signup/logout/', views.logout, name="logout"),
    path('renderLogin/signup/CT_signup/logout/', views.logout, name="logout"),
    path('renderLogin/login/logout/', views.renderLogin, name="logout"),
    re_path('(logout)/$', views.logout, name="logout"),
]