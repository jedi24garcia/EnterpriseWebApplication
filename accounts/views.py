from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SignUpForm, ProfileForm
from .models import Profile
from django import forms

# Create your views here.

# Defining login page
def UserLogin(request):
    if request.method == 'POST':
        # form = LoginForm(request, data=request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')  # Redirect to home after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Defining signup page
def UserSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')  # Redirect to home after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def UserProfile(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = ProfileForm(request.POST or None, instance =current_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
            return redirect('home')
        return render (request, "profile.html", {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')