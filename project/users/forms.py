from django.contrib.auth.models import User
from django import forms
class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    referral_username = forms.CharField(required=False)
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)