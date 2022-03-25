from audioop import add
from django.utils import timezone
from django.forms import PasswordInput
from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import (
    User,
    Blood_info,
)

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate

from .utils import (
    IsLoggedIn,
)

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.

def login(request):
    user = IsLoggedIn(request)
    if user is None:
        return render(request,"public.html")
    else:
        return HttpResponseRedirect("/user/dashboard")

def dashboard(request):
    user = IsLoggedIn(request)
    HttpResponse("User logged in")