from django.shortcuts import render, redirect
from home.models import People
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')

def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'services.html')

def loginUser(request):
    if request.method == "POST":
        # print("POST Request Detected")
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print("Username and Password is: " + username +" " + password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Incorrect Credetentials')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
