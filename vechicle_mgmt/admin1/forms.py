from django.forms import ModelForm
from  django import forms
from admin1.models import Customer,Device
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        widgets={
            "cust_name":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "phone_no": forms.TextInput(attrs={"class": "form-control"})
        }
class DeviceForm(ModelForm):
    class Meta:
        model=Device
        fields="__all__"
        widgets={
            "devicename":forms.TextInput(attrs={"class":"form-control"}),
            "imei":forms.TextInput(attrs={"class":"form-control"}),
            "primarysim":forms.TextInput(attrs={"class":"form-control"}),
            "secondarysim": forms.TextInput(attrs={"class": "form-control"})
        }
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["username","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"})
        }
class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
