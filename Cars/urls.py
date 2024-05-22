from django.urls import path
from . import views



urlpatterns = [
    path("cars/", views.cars_list, name="cars_list"),
    path("cars/add/", views.car_add, name="car_add"),
    path("cars/<int:pk>/", views.car_edit, name="car_edit"),
    path("cars/list/api/", views.CarListAPI.as_view(), name="car_list_api"),
    path("cars/detail/api/<int:pk>/", views.CarDetailAPI.as_view(), name="car_detail_api"),

]

