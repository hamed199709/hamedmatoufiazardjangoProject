from django.shortcuts import render, get_object_or_404
from . models import Car


def viewCar(request):
    car_record=Car.objects.all()
    return render(request,'cars/cars_list.html',{'car_records':car_record})
def viewCarDetails(request,s):
    car_detail=get_object_or_404(Car,slug=s)
    return render(request,'cars/car_details.html',{'car_details':car_detail})