from unicodedata import name
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.renderIndex, name='index'),
    path('schedule/', views.schedules, name="schedule"),
    path('schedule/back/', views.back, name="back"),
    re_path(r'index/heart=(?P<id>[0-9][0-9])/$', views.heart, name="heart"),
    re_path(r'index/add_book=(?P<id>[0-9][0-9])/$', views.schedules, name="book"),
    re_path(r'index/add_book=(?P<id>[0-9][0-9])/back/$', views.back, name="back"),
    re_path(r'index/(?P<id>back)/$', views.back, name='back'),
    path('index/login/', views.checklogin, name="error"),
    path('index/logout/', views.logout, name='logout'),
    re_path(r'index/login/signup/$', views.signup, name='signup'),
    path('index/personal/', views.renderPersonal, name="personal"),
    re_path(r'index/personal/(?P<id>back)/$', views.back, name="personal"),
    
    re_path(r'index/personal/(?P<action>edit_info|edit_profile|create_post)/$', views.edit, name='edit'),
    re_path(r'index/personal/(?P<action>edit_info|edit_profile|create_post)/cancel/$', views.cancel, name='cancel'),
    
    path('index/personal/edit_info/update_info/', views.updata_info, name="update_info"),
    path('index/personal/create_post/update_post/', views.update_post, name="update_post"),
    re_path(r'index/personal/delete=(?P<id>[0-9][0-9])/$', views.delete_post, name="delete_post"),
    
]