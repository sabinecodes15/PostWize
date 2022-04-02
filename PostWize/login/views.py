from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return HttpResponse("User Authentication failed.")
