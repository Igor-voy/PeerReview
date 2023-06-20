from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
#from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm

from .forms import *
from .models import *
# Create your views here.



def index(request):
    return render(request, 'peerreview/index.html', {'title' : 'Главная страница'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('Not found')

#def profile(request):
#    if request.method == 'POST':
#        form = UserProfileForm(data=request)
#        if form.is_valid():
#            form.save()
#           return redirect('profile')
#    else:
#        form = UserProfileForm(isinstance=request)
#    return render(request, 'peerreview/profile.html', {'title': 'Личный кабинет', 'form': form})


class RegisterUser(CreateView):
    #form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'peerreview/register.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'peerreview/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')
    
#class UserProfileView(UpdateView):
#    model = User()
#    form_class = UserProfileForm()
#    template_name = 'profile.html'
#    extra_context = {'title': 'Личный кабинет'}

#    def get_success_url(self):
#        return reverse_lazy('profile', args=(self.object.id,))

def profile(request):
    if request.method == "POST":
        form = UserProfileForm( data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = UserProfileForm()
    context = {'title': 'Профиль', 'form': form} 
    return render(request, 'peerreview/profile.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
