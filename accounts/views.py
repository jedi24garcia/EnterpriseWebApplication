from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm, ProfileForm, UserUpdateForm, ProfileUpdateForm
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
                return redirect('home')  # Redirect to home after login
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
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')  # Redirect to home after signup
        else:
            print("Form is not valid:", form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


#User profile edit

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user.profile)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('user_profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user.profile)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)