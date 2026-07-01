from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "ram", "storage")
    list_filter = ("ram", "storage")
    search_fields = ("name", "description")
    ordering = ("price",)