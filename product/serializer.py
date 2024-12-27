from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer the product response
    """

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        help_text="Provide the Id of an existing category for the product"
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'stock_quantity',
            'category'
        ]


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer the product response
    """

    class Meta:
        model = Category
        fields = [
            'name'
        ]