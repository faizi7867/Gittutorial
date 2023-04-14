from django.urls import path

from loginSystem import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_fun,name='login'),
    path('register',views.register_fun,name='register'),
    path('readlogin',views.login_read),
    path('readregister',views.register_read),
    path('logout',views.logout_fun,name='logout')

]