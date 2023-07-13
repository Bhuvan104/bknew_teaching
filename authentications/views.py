from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser

 

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           CustomUser.objects.create_user( email=form.cleaned_data['email'], password=form.cleaned_data['password'])
           return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegisterForm()

    return render(request, 'registration.html', {'form': form})

