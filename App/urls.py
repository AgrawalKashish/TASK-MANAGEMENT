from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from App import views


urlpatterns = [
    path('' , views.index, name= 'index'),
    path('login', views.login, name= 'login'),
    path('signup', views.signup, name= 'signup'),
    path('add-todo',views.add_todo, name = 'add_todo'),
    path('logout',views.signout, name = 'signout'),
    path('delete-todo/<int:id>',views.delete_todo, name = 'delete_todo'),
    path('edit/<int:id>',views.edit, name = 'edit'),
]