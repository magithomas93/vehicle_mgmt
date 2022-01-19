from django.urls import path
from customer import views


urlpatterns=[
    path("home",views.CustomerHome.as_view(),name="customerhome"),
    path("accounts/signup", views.Registration.as_view(), name="registration"),
    path("accounts/signin", views.SignIn.as_view(), name="signin"),
    path("accounts/signout", views.signout, name="signout")
    ]
