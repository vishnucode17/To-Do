from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as Logout
# Create your views here.
def Home(request):
    return render(request, 'base.html')
def Signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword=request.POST.get('confirmPassword')
            if password == confirmPassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"User already exists")
                    return redirect('/signup')
                else:
                    user=User.objects.create_user(username=username, password=password)
                    user.save()
                    return redirect('/login')
            else:
                messages.info(request,"Password mismatch")
                return redirect('/signup')
        else:
            return render(request, 'accounts/signup.html')

def Login(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')
    return render(request, 'accounts/login.html')

@login_required
def logout(request):
    Logout(request)
    return redirect('/')