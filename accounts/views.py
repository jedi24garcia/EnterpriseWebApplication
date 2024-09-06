from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, SignUpForm

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