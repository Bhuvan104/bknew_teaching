from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser
from django.db import DatabaseError
from django.contrib import messages

 

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                CustomUser.objects.create_user( email=form.cleaned_data['email'], password=form.cleaned_data['password'],role=form.cleaned_data['role'], image = form.cleaned_data['image'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],date_of_birth=form.cleaned_data['date_of_birth'],gender=form.cleaned_data['gender'])
                messages.success(request,'You have registered successfully...!')
                return redirect('/auth/register')  # Redirect to the login page after successful registration
            
            except DatabaseError as e:
                messages.error(request,e.args[1])
                
                 
    else:
        form = RegisterForm()

    return render(request, 'registration.html', {'form': form})

