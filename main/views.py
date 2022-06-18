from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages


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