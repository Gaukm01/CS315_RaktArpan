from audioop import add
from re import M
from django.utils import timezone
from django.forms import PasswordInput
from django.shortcuts import render, redirect, HttpResponseRedirect
import logging

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
    MAKE_PASSWORD,
    CHECK_PASSWORD,
    role_based_redirection,
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
        url = role_based_redirection(request)
        return HttpResponseRedirect(url)

# def public(request):
#     user = IsLoggedIn(request)
#     if user is not None:
#         HttpResponseRedirect("/user/login")

def loginpage(request):
    return render(request,"signin.html")
    # user = IsLoggedIn(request)
    # if user in None:
    #     return render(request,"signin.html")
    # else:
    #     url = role_based_redirection(request)
    #     return HttpResponseRedirect(url)



def blood_bank_signup(request):
    user = IsLoggedIn(request)
    if user is None:
        return render(
            request, "signup.html", 
            {
                "cities" : City.objects.all(),
            }
            )

    else:
        url = role_based_redirection(request)
        return HttpResponseRedirect(url)

def register_blood_bank(request):
    user = IsLoggedIn(request)
    if user is None:
        if request.method == "POST":
            name = request.POST.get("blood_bank_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password")
            password2 = request.POST.get("conf_password")
            address = request.POST.get("address")
            contact = request.POST.get("contact")
            city = City.objects.get(city_id=request.POST.get("city"))
            if(password1 != password2):
                messages.error(request, "Password does not match!")
                return HttpResponseRedirect("/user/signup")   
            else:
                password = MAKE_PASSWORD(password1)
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already in use!")
                    return HttpResponseRedirect("/user/signup")
                elif User.objects.filter(email=email).exists():
                    messages.error(request, "User with this email already exits!")
                    return HttpResponseRedirect("/user/signup")
                else:
                    user = User(roles="blood_bank")
                    user.blood_bank_name = name
                    user.username = username
                    user.email = email
                    user.password = password
                    user.address = address
                    user.contact= contact
                    user.city = city
                    user.save()

                    messages.success(request, "User account created successfully!")
                    return HttpResponseRedirect("/user/loginpage")
        else:
            messages.error(request, "Please fill in the credentials to sign up!")
            return HttpResponseRedirect("/user/signup")
    else: # user is already logged in 
        url = role_based_redirection(request)
        return HttpResponseRedirect(url)

# rendered when logging in using the form on login page
def loginUser(request): 
    user = IsLoggedIn(request)
    if user is None:  # user is not already logged in 
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            if User.objects.filter(username=username).exists(): # username exists in the dB
                user = User.objects.get(username=username)
                if CHECK_PASSWORD(password, user.password): # entered password matches with the password stored in dB
                    request.session["username"] = username
                    request.session.modified = True
                    # rendering pages based on roles
                    url = role_based_redirection(request)
                    return HttpResponseRedirect(url)
                    #return HttpResponseRedirect("/user/dashboard")
                else:
                    messages.error(request, "Incorrect password!") # password does not matches : redirect to login page 
                    return HttpResponseRedirect("/user/loginpage") 
            else: # user is not registered in the database : redirect to sign up page 
                messages.error(request, "User does not exist. Kindly register yourself! ")
                return HttpResponseRedirect("/user/loginpage")
        else:
            messages.error(request, "Please fill in the credentials first to login in!")
            return HttpResponseRedirect("/user/loginpage")
    else: # user is already logged in : redirect to the login page
        url = role_based_redirection(request)
        return HttpResponseRedirect(url)


def logout(request):
    if IsLoggedIn(request) is not None:
        del request.session["username"]
    return HttpResponseRedirect("/user/")

def blood_bank(request):
    return render(
        request,
        "blood_bank_dashboard.html",
        {
            "user": IsLoggedIn(request),
            #"patient": user.objects.get(user=IsLoggedIn(request)),
        },
    )

def blood_bank_dashboard(request):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('myapp')
    data = {"items": []}
    if request.method == "GET":
        state_ = request.GET.get("state")
        city_ = request.GET.get("city")
        blood_group_ = request.GET.get("blood_group")
        blood_component_ = request.GET.get("blood_component")
        logger.info(f"{state_}")
        logger.info(f"{city_}")
        logger.info(f"{blood_group_}")
        logger.info(f"{blood_component_}")
        count = 1
        for t in User.objects.all():
            logger.info(f"{state_} {t.state}")
            if state_ != '' and t.state != state_:
                continue
            if city_ != '' and t.city != city_:
                continue
            if (blood_component_ == '' or blood_component_ == "RBC") and RBC.objects.filter(user=t).exists():
                rbc = RBC.objects.get(user=t)
                data["items"].append({
                    's_no': count,
                    'name': t.blood_bank_name,
                    'blood_component' : 'RBC',
                    'blood_group_apstv' : rbc.quantity_Apstv if (blood_group_ == '' or blood_group_ == 'A+') else 0,
                    'blood_group_angtv' : rbc.quantity_Angtv if (blood_group_ == '' or blood_group_ == 'A-') else 0,
                    'blood_group_bpstv' : rbc.quantity_Bpstv if (blood_group_ == '' or blood_group_ == 'B+') else 0,
                    'blood_group_bngtv' : rbc.quantity_Bngtv if (blood_group_ == '' or blood_group_ == 'B-') else 0,
                    'blood_group_opstv' : rbc.quantity_Opstv if (blood_group_ == '' or blood_group_ == 'O+') else 0,
                    'blood_group_ongtv' : rbc.quantity_Ongtv if (blood_group_ == '' or blood_group_ == 'O-') else 0,
                    'blood_group_abpstv' : rbc.quantity_ABpstv if (blood_group_ == '' or blood_group_ == 'AB+') else 0,
                    'blood_group_abngtv' : rbc.quantity_ABngtv if (blood_group_ == '' or blood_group_ == 'AB-') else 0,
                })
            if (blood_component_ == '' or blood_component_ == "Plasma") and Plasma.objects.filter(user=t).exists():
                plasma = Plasma.objects.get(user=t)
                data["items"].append({
                    's_no': count,
                    'name': t.blood_bank_name,
                    'blood_component' : 'Plasma',
                    'blood_group_apstv' : plasma.quantity_Apstv if (blood_group_ == '' or blood_group_ == 'A+') else 0,
                    'blood_group_angtv' : plasma.quantity_Angtv if (blood_group_ == '' or blood_group_ == 'A-') else 0,
                    'blood_group_bpstv' : plasma.quantity_Bpstv if (blood_group_ == '' or blood_group_ == 'B+') else 0,
                    'blood_group_bngtv' : plasma.quantity_Bngtv if (blood_group_ == '' or blood_group_ == 'B-') else 0,
                    'blood_group_opstv' : plasma.quantity_Opstv if (blood_group_ == '' or blood_group_ == 'O+') else 0,
                    'blood_group_ongtv' : plasma.quantity_Ongtv if (blood_group_ == '' or blood_group_ == 'O-') else 0,
                    'blood_group_abpstv' : plasma.quantity_ABpstv if (blood_group_ == '' or blood_group_ == 'AB+') else 0,
                    'blood_group_abngtv' : plasma.quantity_ABngtv if (blood_group_ == '' or blood_group_ == 'AB-') else 0,
                })
            if (blood_component_ == '' or blood_component_ == "Platelets") and Platelets.objects.filter(user=t).exists():
                platelets = Platelets.objects.get(user=t)
                data["items"].append({
                    's_no': count,
                    'name': t.blood_bank_name,
                    'blood_component' : 'Platelets',
                    'blood_group_apstv' : platelets.quantity_Apstv if (blood_group_ == '' or blood_group_ == 'A+') else 0,
                    'blood_group_angtv' : platelets.quantity_Angtv if (blood_group_ == '' or blood_group_ == 'A-') else 0,
                    'blood_group_bpstv' : platelets.quantity_Bpstv if (blood_group_ == '' or blood_group_ == 'B+') else 0,
                    'blood_group_bngtv' : platelets.quantity_Bngtv if (blood_group_ == '' or blood_group_ == 'B-') else 0,
                    'blood_group_opstv' : platelets.quantity_Opstv if (blood_group_ == '' or blood_group_ == 'O+') else 0,
                    'blood_group_ongtv' : platelets.quantity_Ongtv if (blood_group_ == '' or blood_group_ == 'O-') else 0,
                    'blood_group_abpstv' : platelets.quantity_ABpstv if (blood_group_ == '' or blood_group_ == 'AB+') else 0,
                    'blood_group_abngtv' : platelets.quantity_ABngtv if (blood_group_ == '' or blood_group_ == 'AB-') else 0,
                })
            if (blood_component_ == '' or blood_component_ == "Cryo AHF") and CryoAHF.objects.filter(user=t).exists():
                cryo_ahf = CryoAHF.objects.get(user=t)
                data["items"].append({
                    's_no': count,
                    'name': t.blood_bank_name,
                    'blood_component' : 'CryoAHF',
                    'blood_group_apstv' : cryo_ahf.quantity_Apstv if (blood_group_ == '' or blood_group_ == 'A+') else 0,
                    'blood_group_angtv' : cryo_ahf.quantity_Angtv if (blood_group_ == '' or blood_group_ == 'A-') else 0,
                    'blood_group_bpstv' : cryo_ahf.quantity_Bpstv if (blood_group_ == '' or blood_group_ == 'B+') else 0,
                    'blood_group_bngtv' : cryo_ahf.quantity_Bngtv if (blood_group_ == '' or blood_group_ == 'B-') else 0,
                    'blood_group_opstv' : cryo_ahf.quantity_Opstv if (blood_group_ == '' or blood_group_ == 'O+') else 0,
                    'blood_group_ongtv' : cryo_ahf.quantity_Ongtv if (blood_group_ == '' or blood_group_ == 'O-') else 0,
                    'blood_group_abpstv' : cryo_ahf.quantity_ABpstv if (blood_group_ == '' or blood_group_ == 'AB+') else 0,
                    'blood_group_abngtv' : cryo_ahf.quantity_ABngtv if (blood_group_ == '' or blood_group_ == 'AB-') else 0,
                })
            if (blood_component_ == '' or blood_component_ == "Granulocytes") and Granulocytes.objects.filter(user=t).exists():
                granulocytes = Granulocytes.objects.get(user=t)
                data["items"].append({
                    's_no': count,
                    'name': t.blood_bank_name,
                    'blood_component' : 'Granulocytes',
                    'blood_group_apstv' : granulocytes.quantity_Apstv if (blood_group_ == '' or blood_group_ == 'A+') else 0,
                    'blood_group_angtv' : granulocytes.quantity_Angtv if (blood_group_ == '' or blood_group_ == 'A-') else 0,
                    'blood_group_bpstv' : granulocytes.quantity_Bpstv if (blood_group_ == '' or blood_group_ == 'B+') else 0,
                    'blood_group_bngtv' : granulocytes.quantity_Bngtv if (blood_group_ == '' or blood_group_ == 'B-') else 0,
                    'blood_group_opstv' : granulocytes.quantity_Opstv if (blood_group_ == '' or blood_group_ == 'O+') else 0,
                    'blood_group_ongtv' : granulocytes.quantity_Ongtv if (blood_group_ == '' or blood_group_ == 'O-') else 0,
                    'blood_group_abpstv' : granulocytes.quantity_ABpstv if (blood_group_ == '' or blood_group_ == 'AB+') else 0,
                    'blood_group_abngtv' : granulocytes.quantity_ABngtv if (blood_group_ == '' or blood_group_ == 'AB-') else 0,
                })
            count += 1
    return render(request, "blood_bank_dashboard.html",data)