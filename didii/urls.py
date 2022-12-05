from unicodedata import name
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.renderIndex, name='index'),
    re_path(r'index/(?P<action>[0-9][0-9]/|back/)$', views.checklogin, name="error"),
    path('index/login/', views.checklogin, name="login"),
    path('index/login/logout/', views.logout, name='logout'),
    path('index/login/back/', views.back, name='back'),
    re_path(r'index/login/signup/$', views.signup, name='signup'),
    re_path(r'index/login/(?P<id>[0-9][0-9])/$', views.heart, name="heart"),
    path('index/login/personal/', views.renderPersonal, name="personal"),
    
    re_path(r'index/login/personal/(?P<action>edit_info|edit_profile|create_post)/$', views.edit, name='edit'),
    re_path(r'index/login/personal/(?P<action>edit_info|edit_profile|create_post)/cancel/$', views.cancel, name='cancel'),
    
    path('index/login/personal/edit_info/update_info/', views.updata_info, name="update_info"),
    path('index/login/personal/create_post/update_post/', views.update_post, name="update_post"),
    
    path('index/signup/signup/personal/', views.renderPersonal, name="personal"),
    re_path(r'index/signup/signup/personal/(?P<action>edit_info|edit_profile|create_post)/$', views.edit, name="edit"),
    re_path(r'index/signup/signup/personal/(?P<action>edit_info|edit_profile|create_post)/cancel/$', views.cancel, name="cancel"),
    
    path('index/signup/signup/logout/', views.logout, name="logout"),
    re_path(r'index/(?P<action>\w+/)/$', views.logout, name="logout"),
]