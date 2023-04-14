from django.shortcuts import render, redirect

from studentmarksapp.models import City, Course, Student


# Create your views here.
def index(request):
    return None


def addstudent(request):
    cities=City.objects.all()
    courses=Course.objects.all()
    s1 = Student.objects.all()
    return render(request,'addstudent.html',
                  {'cities':cities,'courses':courses})


def readstudentfun(request):
    s1=Student()
    s1.fname=request.POST['tbfname']
    s1.lname=request.POST['tblname']
    s1.mobile=request.POST['tbnum']
    s1.email=request.POST['tbemail']
    s1.city=City.objects.get(city_name=request.POST['ddlcity'])
    s1.course=Course.objects.get(course_name=request.POST['ddlcourse'])
    s1.save()
    return redirect('displaystudent')


def displayfun(request):
    s1=Student.objects.all()
    return render(request,'displaystudent.html',{'data':s1})


def updatestudent(request,id):
    cities = City.objects.all()
    courses = Course.objects.all()
    s1 = Student.objects.get(id=id)
    if request.method=='POST':
        s1.fname = request.POST['tbfname']
        s1.lname = request.POST['tblname']
        s1.mobile = request.POST['tbnum']
        s1.email = request.POST['tbemail']
        s1.city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.save()
        return redirect('displaystudent')
    return render(request,'updatestudent.html',
                  {'data':s1,'cities':cities,'courses':courses})


def deletestudent(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('displaystudent')


