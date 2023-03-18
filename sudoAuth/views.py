from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.urls import reverse 
from django.http import HttpResponseRedirect
# Create your views here.


def login(request): 
    return render(request,'login.html')

@login_required
def home(request) :
    return render(request,'home.html',{'user':request.user})

def index() :
    return "Hey there"


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return HttpResponseRedirect(reverse('login'))

