from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(req):
    if req.method == 'POST':
        #signup user
        if req.POST['password1'] == req.POST['password2']:
            try:
                user = User.objects.get(username=req.POST["email"])
                return render (req,"accounts/signup.html",{'error':'User already exists!'})
            except User.DoesNotExist:
                user = User.objects.create_user(req.POST['email'], password = req.POST['password1'])
                auth.login(req,user)
                return redirect('home')
        else:
            return render(req,"accounts/signup.html",{'error':'Passwords do not match!'})
    else:
        return render(req,"accounts/signup.html")

def login(req):
    if req.method == 'POST':
        user = auth.authenticate(username=req.POST['email'],password=req.POST['password'])
        if user:
            auth.login(req,user)
            return redirect('home')
        else:
            return render(req,'accounts/login.html',{'error': 'Invalid email or password!'})
    else:
        return render(req,"accounts/login.html")

def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        return redirect('home')
