from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer