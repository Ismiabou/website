from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserRegistration, UserLoginForm, ProfileForm
from .models import Profile


def user_register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('edit-profile')
    else:
        form = UserRegistration()
    return render(request, "Registration/register.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        finally:
            messages.error(request, 'Invalid username, please provide a valid username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'Registration/login.html', context)


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login/')


@login_required(login_url='login')
def update_profile(request):
    query = request.user.username
    pro = Profile.objects.get(username=query)
    form = ProfileForm(instance=pro)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=pro)
        if form.is_valid:
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'Registration/profile.html', context)


@login_required(login_url='login')
def account(request):
    query = request.user.username
    pro = Profile.objects.filter(username=query)
    context = {'pro': pro}
    return render(request, 'Registration/account.html', context)


@login_required(login_url='login')
def user_delete(request):
    query = request.user.username
    user = User.objects.get(username=query)
    if request.method == 'POST':
        user.delete()
        logout(request)
    return redirect('login')
