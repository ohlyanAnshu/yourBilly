from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'billy/base.html')

def login(request):
    return render(request, 'billy/login.html')

def signup(request):
    return render(request, 'billy/signup.html')
