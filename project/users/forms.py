from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    referral_username = forms.CharField(required=False)
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    def clean_referral_username(self):
        referral_username = self.cleaned_data.get('referral_username')
        if referral_username:        	
	        qs = User.objects.filter(username=referral_username)
	        if not qs.exists():
	            raise forms.ValidationError("referal username does not exist")
	        return referral_username



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput( 
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password :
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid Log in details. Try Again....")
            if not user.is_active:
                raise forms.ValidationError("This User is no longer active.")
            return super(LoginForm, self).clean(*args, **kwargs)