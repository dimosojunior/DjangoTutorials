from django.contrib import admin
from .models import Products


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display= ["name", "price", "post_date", "brand"]
    search_fields = ["name", "post_date"]
    list_filter = ["price", "post_date"]
admin.site.register(Products, ProductsAdmin)
