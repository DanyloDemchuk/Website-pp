from .models import Car
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "owner", "plate", "car_name", "max_speed"]
