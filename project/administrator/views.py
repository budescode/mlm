from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Profile

@login_required(login_url='/users/login/')
def administrator(request):
	qs = Profile.objects.get(user=request.user)
	return render(request, 'administrator/index.html', {'qs':qs})