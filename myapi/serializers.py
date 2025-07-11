# myapi/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    Converts Product model instances to JSON and vice versa.
    """
    class Meta:
        model = Product
        # Fields to include in the serialized output.
        # '__all__' includes all fields from the model.
        # Alternatively, you can list specific fields:
        # fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at']
        fields = '__all__'
