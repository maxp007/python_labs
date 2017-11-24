from django import forms
from .models import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        exclude = ["computers", "login", "password", "secondname", "firstname"]

    firstname =  forms.CharField(label="Имя", )
    secondname = forms.CharField(label="Фамилия", )
    email = forms.EmailField(label="e-mail")
    login = forms.CharField(min_length=5, label="Логин", )
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль", )
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль", )


class AuthorizeForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        exclude = ["computers", "firstname", "secondname", "email"]

    login = forms.CharField(min_length=5, label="Логин", )
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль", )