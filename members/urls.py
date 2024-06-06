from django.urls import path

from members import views
app_name='members'

urlpatterns=[
    path('',views.user_register,name='user-register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('cp/',views.viewchangepassword,name='viewchangepassword'),


]