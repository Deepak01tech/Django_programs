from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import employee
# Register your models here.


# admin.site.register(employee)

@admin.register(employee)
class EmployeeAdmin(ModelAdmin):
    list_display = [
        "name",
        'email',
    ]
    search_fields = [
        "name",
        "email",
    ]


