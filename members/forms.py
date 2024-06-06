from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'enter user name'}))
    email=forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'placeholder':'enter email'}))
    firstname=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'enter first name'}))
    lastname=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'enter last name'}))
    password_1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))
    password_2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'enter password again'}))

    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exists')
        return user

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exists')
        return email

    def clean_password_2(self):
        pass1 = self.cleaned_data['password_1']
        pass2 = self.cleaned_data['password_2']
        if pass1 != pass2:
            raise forms.ValidationError('password not match')
        elif len(pass2) < 8:
            raise forms.ValidationError('password was short.')
        elif not any(i.isupper() for i in pass2):
            raise forms.ValidationError('at least be Upper')
        return pass2


#------------------------------- form Login

class UserLoginForm(forms.Form):
    user=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'please user'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'please password'}))


class ChangePasswordForm(forms.Form):
    old_pass=forms.CharField(widget=forms.PasswordInput())
    new_pass1 = forms.CharField(widget=forms.PasswordInput())
    new_pass2 = forms.CharField(widget=forms.PasswordInput())