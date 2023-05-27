
from django.urls import path
from . import views

app_name='homepage'
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.register,name='register'),
    path('form/',views.form,name='form'),
    path('regform/',views.regform,name='regform'),
    path('confirm/',views.confirm,name='confirm'),


]