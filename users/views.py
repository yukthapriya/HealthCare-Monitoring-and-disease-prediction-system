from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for { username }!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def save(request):
    user = User.objects.get(username=request.user.username)
    Profile.objects.create(user=user)
    return redirect('home')