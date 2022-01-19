from django.urls import path
from admin1 import views

urlpatterns=[
    path("",views.AdminHome.as_view(),name="adminhome"),
    path("user/add",views.AddMobile.as_view(),name="adduser"),
    path("device/add",views.AddDevice.as_view(),name="adddevice"),
    path("accounts/signup", views.Registration.as_view(), name="registration"),
    path("accounts/signin", views.SignIn.as_view(), name="signin"),
    path("accounts/signout", views.signout, name="signout")
    ]