from django.shortcuts import render,get_object_or_404,redirect
from . models import Department,Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password=request.POST.get('password')

        user =  authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('form/')
        else:
            messages.info(request,'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html',context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)
            return redirect('login/')
    context ={'form':form}
    return render(request, 'register.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login/')

def form(request):
    return render(request, 'form.html')

def regform(request):
   return render(request, 'regform.html')

def confirm(request):
    return render(request, 'confirm.html')


