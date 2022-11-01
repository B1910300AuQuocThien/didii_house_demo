from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.renderIndex, name='index'),
    path('renderLogin/', views.renderLogin, name='renderLogin'),
    path('renderLogin/login/', views.checklogin, name="login"),
    path('index/login/', views.login, name="login"),
    path('renderLogin/signup/', views.renderSignup, name="signup"),
    path('renderLogin/signup/CT_signup/', views.CT_signup, name="CT_signup"),
    path('renderLogin/login/logout/', views.logout, name="logout"),
]