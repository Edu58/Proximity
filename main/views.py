from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request, 'index.html')


def signup_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

        messages.warning(request, 'Please provide the required credentials!')
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    form = LoginUserForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')

        messages.warning(request, 'Invalid email or password!')
    return render(request, 'login.html', {'form': form})