from django.shortcuts import render

def home(req):
    return render(req,'products/home.html')
