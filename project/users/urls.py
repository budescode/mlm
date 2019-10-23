from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'users'


urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    

]
