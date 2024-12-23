from django.contrib import admin
from .models import UserData
from django.contrib.admin import ModelAdmin
# Register your models here.


# admin.site.register(UserData)

@admin.register(UserData)
class UserAdmin(ModelAdmin):
    list_display = [
        "name",
        'email',
    ]
    search_fields = [
        "name",
        "email",
    ]



