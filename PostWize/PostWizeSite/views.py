import email
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django import forms
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'app/dashboard.html')

def dashboard(request):
    #return HttpResponse("Hello, world! This is the dashboard.")
    return render(request, 'app/dashboard.html')

def signup(request):
    return render(request, 'registration/signup.html')

def login_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            user_email = form.data['email']
            password = form.data['password']
            user = authenticate(email=user_email, password=password)

            if user is not None:
                login(request, user)
            else:
                return HttpResponse("Authentication Failed")
    else:
        form = UserForm()  
    return render(request, 'registration/login.html', {'form': form})

# def parse_creds(request):
#     if request.method == POST:
        
    # email = request.POST['email']
    # password = request.POST['password']

    # user = authenticate(email=email, password=password)

    # if user is not None:
    #     login(request, user)
    #     redirect(dashboard(request))
    # else:
    #     return HttpResponse("Authentication Failed")
