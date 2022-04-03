from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app/dashboard.html')

def dashboard(request):
    #return HttpResponse("Hello, world! This is the dashboard.")
    return render(request, 'app/dashboard.html')

def signup(request):
    return render(request, 'registration/signup.html')

def login(request):
    return render(request, 'registration/login.html')
