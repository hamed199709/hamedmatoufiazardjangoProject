from django import forms


class UserCommentForm(forms.Form):
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'placeholder': 'example:jack@gmail.com'}))
    firstname = forms.CharField(max_length=30,  widget=forms.TextInput(attrs={'placeholder': 'example:sara'}))
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'example:stark'}))
    comment = forms.CharField(max_length=550, widget=forms.Textarea(attrs={'placeholder': 'example:this site is perfect'}))

