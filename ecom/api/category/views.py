from django.shortcuts import render
from .serializers import CategorySerializer
from django.http import JsonResponse
from .models import Category
from rest_framework import viewsets
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


