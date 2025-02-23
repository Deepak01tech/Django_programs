from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['username', 'email']

    search_fields = ["username", "email"]
