from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from Student.models import Student, City, Course

@login_required
def home(request):
    return redirect('displaystudent')

@login_required
def displaystudent(request):
    return render(request,'displaystudent.html',{'students':Student.objects.all()})

@login_required
def addstudent(request):
    cities = City.objects.all()
    courses = Course.objects.all()
    return render(request,'addstudent.html',{'cities':cities,'courses':courses})


def readstudentdata(request):
    s = Student()
    s.fname = request.POST['tbfname']
    s.lname = request.POST['tblname']
    s.mobile = request.POST['tbmobile']
    s.email = request.POST['tbemail']
    s.city = City.objects.get(city_name = request.POST['ddlcity'])
    s.course = Course.objects.get(course_name = request.POST['ddlcourse'])
    s.save()
    return redirect('displaystudent')


def updatestudent(request,id):
    return None


def deletestudent(request,id):
    return None