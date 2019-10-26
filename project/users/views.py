from django.shortcuts import render, redirect
from .forms import UserRegistrationForm 
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm
from django.contrib.auth import authenticate, login, get_user_model, logout

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data['username']
			referral_username = form.cleaned_data['referral_username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			print(username, referral_username, email, password)
			user = User.objects.create_user(username, email, password)
			if referral_username:
				
				try:					
					referal_1 = User.objects.get(username=referral_username)
					referal1 = Profile.objects.get(user=referal_1)				
					referal1.level1 = referal1.level1 + 50
					referal1.save()
					print('referal1', referal_1)
				except:
					...

				try:					
					referal2_user = referal1.referal.username
					print(referal2_user, 'referal2')
					referal_2 = User.objects.get(username = referal2_user)
					referal2 = Profile.objects.get(user=referal_2)				
					referal2.level2 = referal2.level2  +  50
					referal2.save()
				except:
					...
				try:
					referal3_user = referal2.referal.username
					print(referal3_user, 'referal3')
					referal_3 = User.objects.get(username = referal3_user)
					referal3 = Profile.objects.get(user=referal_3)				
					referal3.level3 = referal3.level3  +  50
					referal3.save()
				except:
					...

				try:
					referal4_user = referal3.referal.username
					print(referal4_user, 'referal4')
					referal_4 = User.objects.get(username = referal4_user)
					referal4 = Profile.objects.get(user=referal_4)				
					referal4.level4 = referal4.level4  +  50
					referal4.save()
				except:
					...

				try:
					referal5_user = referal4.referal.username
					print(referal5_user, 'referal5')
					referal_5 = User.objects.get(username = referal5_user)
					referal5 = Profile.objects.get(user=referal_5)				
					referal5.level5 = referal5.level5  +  50
					referal5.save()
				except:
					...

				Profile.objects.create(user=user, referal=referal_1)
			else:
				Profile.objects.create(user=user)

			return redirect('users:login_page')
			
	else:
		form = UserRegistrationForm()
	context = {'form':form}
	return render(request, 'administrator/register.html', context)




def logout_page(request):
	logout(request)
	return render(request, "administrator/logout.html", {})



def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		return redirect('/')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context = {"form": form}
	return render(request, "administrator/login.html", context)