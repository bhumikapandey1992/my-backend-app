# myapi/models.py
from django.db import models

class Product(models.Model):
    """
    Represents a product in the catalog.
    Each product has a name, description, price, and a stock quantity.
    """
    name = models.CharField(max_length=255, help_text="Name of the product")
    description = models.TextField(blank=True, null=True, help_text="Detailed description of the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the product")
    stock = models.IntegerField(default=0, help_text="Current stock quantity")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the product was added")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp of the last update")

    class Meta:
        # Orders products by name by default
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        """
        String representation of the Product model, useful for Django Admin.
        """
        return self.name

