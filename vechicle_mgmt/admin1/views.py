from django.shortcuts import render,redirect
from admin1.models import Customer,Device
from django.contrib.auth import authenticate,login,logout
from admin1.decorators import signin_required
from django.views.generic import View,TemplateView,CreateView
from admin1 import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

@method_decorator(signin_required,name="dispatch")
class AdminHome(View):
    template_name='admin_home.html'
    def get(self,request,**kwargs):
        return render(request,self.template_name)

@method_decorator(signin_required,name="dispatch")
class AddMobile(View):
    model=Customer
    template_name='add_user.html'
    form_class=forms.CustomerForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('adduser')
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

@method_decorator(signin_required,name="dispatch")
class AddDevice(View):
    model=Device
    template_name='add_device.html'
    form_class=forms.DeviceForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('adddevice')
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

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
                    return redirect("adminhome")
                else:
                    return redirect("adminhome")
            else:
                print("invalid")

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



