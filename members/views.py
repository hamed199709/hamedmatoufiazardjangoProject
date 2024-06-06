from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_register(request):
    if request.method=='POST':
        form_register=UserRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['firstname'],
                                     last_name=data['lastname'],
                                     password=data['password_1'])
            return HttpResponse('your registration was successfully')
    else:
        form_register=UserRegisterForm()
    return render(request,'members/register.html',{'form_registers':form_register})


#------------------------------Login

def user_login(request):
    if request.method == 'POST':
        form_login=UserLoginForm(request.POST)
        if form_login.is_valid():
            data=form_login.cleaned_data
            user=authenticate(username=data['user'],password=data['password'])
            if user is not None:
                login(request,user)
                return HttpResponse('your login was successfully')
    else:
        form_login=UserLoginForm()
    return render(request,'members/login.html',{'form_login':form_login})


#------------------------------logout

def user_logout(request):
    logout(request)
    return redirect('home')



@login_required()
def viewchangepassword(request):
    if request.method == 'POST':
        user=request.user
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            old_pass = data['old_pass']
            new_pass1 = data['new_pass1']
            new_pass2 = data['new_pass2']
            if not user.check_password(old_pass):
                return HttpResponse('incorrect password.')
            elif new_pass1!=new_pass2 :
                return HttpResponse('password not match.')
            else:
                user.set_password(new_pass1)
                login(request,user)
                user.save()
                return HttpResponse('done.')
    else:
        form=ChangePasswordForm()

    return render(request,'members/changepassword.html',{'form':form})