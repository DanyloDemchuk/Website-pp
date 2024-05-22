from django.shortcuts import render, redirect, get_object_or_404

from Users.forms import MemberEditForm
from .forms import CarForm, CarEdit
from .models import Car
from .serializers import CarSerializer
from rest_framework import generics
from Users.decorators import check_login


def cars_list(request):
    print("Користувач авторизований. Ідентифікатор сесії:", request.session.session_key)
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, "cars_list.html", context)


def car_add(request):
    print("Користувач авторизований. Ідентифікатор сесії:", request.session.session_key)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cars_list")
    else:
        form = CarForm()
    return render(request, "car_add.html" ,{"form":form})


def car_edit(request, pk):
    print("Користувач авторизований. Ідентифікатор сесії:", request.session.session_key)
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarEdit(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("cars_list")

    else:
        form = CarEdit(instance=car)
    return render(request, "car_edit.html", {"form":form})


class CarListAPI(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer