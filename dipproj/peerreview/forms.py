from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
#from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'})), 
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'})), 
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'})), 
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'})), 
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'})), 
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'})),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(), 
            'first_name': forms.TextInput(), 
            'last_name': forms.TextInput(), 
            'email': forms.TextInput(), 
            'password1': forms.PasswordInput(), 
            'password2': forms.PasswordInput(),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'})), 
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'})),

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control py-4'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control py-4'}))
    image = forms.ImageField(widget = forms.FileInput(attrs = {'class': 'custom-file-input'}), required=False)
    usernme = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')