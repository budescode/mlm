from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'administrator'


urlpatterns = [

    path('', views.administrator, name='administrator'),

]
