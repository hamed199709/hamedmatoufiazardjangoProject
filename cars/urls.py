from django.urls import path

from cars import views

urlpatterns=[
    path('',views.viewCar,name='viewCar'),
    # path('<int:car_id>',views.viewCarDetails,name='viewCarDetails'),
    path('<slug:s>',views.viewCarDetails,name='viewCarDetails'),

]
