# myapi/admin.py
from django.contrib import admin
from .models import Product

# Register your models here.
# This makes the Product model visible and manageable in the Django admin interface.
admin.site.register(Product)

# You can also customize the admin interface further, e.g.:
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock', 'created_at')
#     search_fields = ('name', 'description')
#     list_filter = ('created_at', 'updated_at')
