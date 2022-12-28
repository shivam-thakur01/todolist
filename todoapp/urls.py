from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('home/',views.signup,name='signup'),
    path('addtask/',views.addtask,name='addtask'),
    path('showtask/',views.showtask,name='showtask'),
    path('navtoaddtask/',views.navtoaddtask,name='navtoaddtask'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('status/',views.statusChange,name='status'),
    path('signuppage/',views.signuppage),
    path('loginpage/',views.loginpage)
]