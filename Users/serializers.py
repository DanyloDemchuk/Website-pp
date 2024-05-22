from .models import Member
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "first_name", "last_name", "username", "email", "password"]