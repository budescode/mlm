from django.shortcuts import render

# Create your views here.
def administrator(request):
	return render(request, 'administrator/index.html')