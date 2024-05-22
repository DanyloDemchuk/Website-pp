from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ("owner", "car_name", "plate", "max_speed")
    list_filter = ("max_speed",)


admin.site.register(Car, CarAdmin)