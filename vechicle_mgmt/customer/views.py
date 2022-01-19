from django.shortcuts import render,redirect
from admin1.models import Customer,Device
from django.contrib.auth import authenticate,login,logout
from admin1.decorators import signin_required
from django.views.generic import View,TemplateView,CreateView,ListView
from admin1 import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

class CustomerHome(ListView):
    model=Customer
    template_name="custom_home.html"
    context_object_name = "users"
class Registration(CreateView):
    template_name='registration.html'
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy("signin")
    model = User

class SignIn(TemplateView):
    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        form=forms.SigninForm()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data["username"]
            pwd=form.cleaned_data["password"]
            user=authenticate(request,username=u_name,password=pwd)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect("customerhome")
                else:
                    return redirect("customerhome")
            else:
                print("invalid")

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")