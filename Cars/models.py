from django.core.validators import RegexValidator
from django.db import models
from Users.models import Member
class Car(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='cars', blank=False)
    plate_regex = r"^[A-Z]{2}\s\d{4}\s[A-Z]{2}$"
    plate = models.CharField(max_length=10, blank=False, validators=[RegexValidator(regex=plate_regex, message="Формат номерів XX 1111 XX")])
    car_name = models.CharField(max_length=20, blank=False)
    max_speed = models.IntegerField(default=100)

    def __str__(self):
        return self.plate







