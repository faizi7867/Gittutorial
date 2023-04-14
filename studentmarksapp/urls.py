from django.urls import path

from studentmarksapp import views

urlpatterns=[
    path('',views.index,name='home'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('readstudent',views.readstudentfun,name='readstudentdata'),
    path('displaystudent',views.displayfun,name='displaystudent'),
    path('update/<int:id>',views.updatestudent,name='update'),
    path('delete/<int:id>', views.deletestudent, name='delete'),

]