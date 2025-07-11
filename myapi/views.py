# myapi/views.py
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# We no longer need APIView, Response, status from previous HelloApiView

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    Provides CRUD operations for the Product model.
    """
    # Define the queryset: retrieve all Product objects from the database.
    queryset = Product.objects.all()
    # Define the serializer class to use for converting Product instances.
    serializer_class = ProductSerializer

    # You can add custom logic here if needed, e.g., for permissions or filtering.
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user) # Example if you had user authentication
