from collections import UserDict
from datetime import date
from django.contrib.auth import authenticate, login as loginuser, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from App.forms import TODOForm
from App.models import TODO

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user)
        return render(request, 'index.html', context={'form' : form, 'todos' : todos})
    else:
        return redirect('index')


def login(request):
    if request.method=='GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, 'login.html' , context=context)
    
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
         username =    form.cleaned_data.get('username')
         password =    form.cleaned_data.get('password')
         user     =    authenticate(username = username, password = password)
         
         if user is not None:
             loginuser(request,user)
             return redirect('index')
        
        else:
             context = {
            "form" : form
        }
        return render(request, 'login.html' , context=context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
                }
        return render(request, 'signup.html', context=context)

    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('index')
            
        else:
            context = {
            "form" : form
                }
            return render(request, 'signup.html', context=context)
            
            
            
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.date = date
            todo.save()
            print(todo)
            return redirect("index")
        else:
            
            return render(request, 'index.html', context={'form' : form})



@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')


def delete_todo(request,id):
    TODO.objects.get(pk = id).delete()
    
    return redirect('index')

def edit(request,id):
      todo =  TODO.objects.get(pk = id)
      form = TODOForm(instance=todo)
      
      if request.method == "POST":
          form = TODOForm(request.POST, instance=todo)
          if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = UserDict
            todo.date = date
            todo.save(pk = id)
            return redirect("index")
      else:
        return render(request, 'index.html', context={'form' : form})
        
  