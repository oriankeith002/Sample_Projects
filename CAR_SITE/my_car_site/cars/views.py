from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.

def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    return render(request, 'cars/list.html',context=context)

def add(request):
    # print(request.POST) # prints out a POST query data.
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        model.Car.objects.create(brand=brand,year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.POST:
        #delete the car
        pk = request.POST['pk']
        try:
            models.Car.object.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('PK not Found')
            return redirect(reverse('cars:list')) # if pk is out of range
    else:
        return render(request, 'cars/delete.html')

    