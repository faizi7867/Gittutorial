from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(requent):
    return render(requent, 'home.html')


def login_fun(request):
    return render(request, 'login.html')


def login_read(request):
    unmae = request.POST['tbusername']
    user_password = request.POST['tbpass']
    myuser = authenticate(username=unmae, password=user_password)
    print(myuser)
    if myuser is not None:
        login(request, myuser)
        return redirect('displaystudent')
    else:
        return render(request, 'login.html', {'data': 'invalid username or password'})


def register_fun(request):
    return render(request, 'register.html')


def register_read(request):
    uname = request.POST['tbusername']
    useremail = request.POST['tbemail']
    userpswd = request.POST['tbpass']
    user = User.objects.create_superuser(email=useremail, password=userpswd, username=uname)
    user.save()
    return render(request, 'login.html', {'name': user,'msg':f"user created sucessfully"})


def logout_fun(request):
    logout(request)
    return redirect('login')