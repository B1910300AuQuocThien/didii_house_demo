from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('myfirst/', views.myfirst, name='myfirst'),
    path('variable/', views.variable, name='variable'),
    path('condition/', views.condition, name='condition'),
    path('forloop/', views.forloop, name='forloop'),
    path('forloop/goback/', views.goback, name='goback'),
    path('cycle/', views.cycle, name='cycle'),
    path('cycle/goback/', views.goback, name='goback'),
    path('mymaster/', views.mymaster, name='mymaster'),
    path('mymaster/goback/', views.goback, name='goback'),
    path('add/addHouse/', views.addHouse, name='addHouse'),
    path('delete/<int:id>', views.deleteHouse, name='deleteHouse'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updateHouse/<int:id>', views.updateHouse, name='updateHouse'),
    path('include/', views.include, name='include'),
    path('include/goback/', views.goback, name='goback')
]