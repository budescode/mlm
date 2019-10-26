from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'users'


urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    
    

]
