from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "password", "username")


admin.site.register(Member,MemberAdmin)
