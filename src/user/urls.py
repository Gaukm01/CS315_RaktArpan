from django.urls import path
from . import views

urlpatterns = [
    path("",views.login, name="login"),
    path("searchBlood",views.searchBlood, name="searchBlood"),
    path("loginpage",views.loginpage, name="loginpage"),
    path("signup", views.blood_bank_signup, name="signup"),
    path("register", views.register_blood_bank, name="register_blood_bank"),
    path("loginUser", views.loginUser, name="loginUser"),
    path("logout", views.logout, name="logout"),
    path("blood_bank_dashboard",views.blood_bank_dashboard, name="blood_bank_dashboard"),
    path("/getdetails", views.getdetails, name="getdetails")
]