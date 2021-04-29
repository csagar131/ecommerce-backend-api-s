from django.shortcuts import render
from .serializers import ProductSerializer
from django.http import JsonResponse
from .models import Product
from rest_framework import viewsets
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer