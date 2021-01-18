from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from accounts.models import User

# Create your views here.

def login(request):
    if request.method=='POST':
        name=request.POST['uname']
        password=request.POST['psw']

        user = auth.authenticate(name=name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid user')
            return redirect('login')
def register(request):
    print("register")
    if request.method=='POST':
        name=request.POST['uname']
        password=request.POST['psw']

        user=user.objects.create_user(name=name,password=password)
        user.save()
        return redirect('login')

        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')