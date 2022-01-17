from django import forms
from .models import Worker
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="User name", widget=forms.TextInput(
        attrs={"class": "form_control"}   
    ))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form_control"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="User name", widget=forms.TextInput(
        attrs={"class": "form_control"}   
    ))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form_control"}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(
        attrs={"class": "form_control"}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(
        attrs={"class": "form_control"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
class CreateWorker(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ["last_name", "first_name", "patronymic",
         "current_department", "current_position", "device_date"]
        widgets = {
            "last_name": forms.TextInput(attrs={"class": "form_control"}),
            "first_name": forms.TextInput(attrs={"class": "form_control"}),
            "patronymic": forms.TextInput(attrs={"class": "form_control"}),
        }
