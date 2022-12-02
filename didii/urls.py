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
    re_path(r'renderLogin/login/personal/(?P<action>edit_info|edit_profile|create_post)/cancel/$', views.cancel, name='cancel'),
    
    path('renderLogin/login/personal/edit_info/update_info/', views.updata_info, name="update_info"),
    path('renderLogin/login/personal/create_post/update_post/', views.update_post, name="update_post"),
    
    
    re_path(r'^renderLogin/\w/[login]*/login/$', views.checklogin, name="login"),
    path('index/login/', views.login, name="login"),
    # re_path(r'^index/login/', views.login, name="login"),
    path('renderLogin/signup/', views.renderSignup, name="signup"),
    path('renderLogin/signup/signup/', views.signup, name="signup"),
    path('renderLogin/signup/signup/personal/', views.renderPersonal, name="personal"),
    
    re_path(r'renderLogin/signup/signup/personal/(?P<action>edit_info|edit_profile|create_post)/$', views.edit, name="edit"),
    re_path(r'renderLogin/signup/signup/personal/(?P<action>edit_info|edit_profile|create_post)/cancel/$', views.cancel, name="cancel"),
    
    path('renderLogin/signup/signup/logout/', views.logout, name="logout"),
    path('renderLogin/login/logout/', views.renderLogin, name="logout"),
    re_path('(logout)/$', views.logout, name="logout"),
]