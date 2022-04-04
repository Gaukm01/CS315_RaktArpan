from audioop import add
from django.utils import timezone
from django.forms import PasswordInput
from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import (
    User,
    City,
    RBC,
    Platelets,
    Plasma,
    CryoAHF,
    Granulocytes
)

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate

from .utils import (
    IsLoggedIn,
)

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import (
    User,
    City,
    RBC,
    Platelets,
    Plasma,
    CryoAHF,
    Granulocytes
)

# Create your views here.

def login(request):
    user = IsLoggedIn(request)
    if user is None:
        return render(request,"public.html")
    else:
        return HttpResponseRedirect("/user/dashboard")

def dashboard(request):
    data = {'items': []}
    for blood_bank_user in User.objects.all():
        data['items'].append({
            "user_id": blood_bank_user.user_id,
            "name": blood_bank_user.blood_bank_name,
            "component":  
        })
    return render(request, "dashboard.html", data)