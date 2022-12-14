from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is my First Django Homepage")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("This is my First Django Homepage")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is my First Django Homepage")
    return render(request, 'services.html')

def login(request):
    # return HttpResponse("This is my First Django Homepage")
    return render(request, 'login.html')