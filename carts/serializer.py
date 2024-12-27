from rest_framework import serializers

from product.serializer import ProductSerializer
from product.models import Product
from carts.models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.
    Handle adding and Viewing the cart items
    """

    product = ProductSerializer(
        read_only=True
    )

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        help_text="prove the id of the product"
    )

    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'product_id',
            'quantity'
        ]
        extra_kwargs = {
            'quantity': {
                'help_text': 'Enter the quantity of the product in the cart.'
            }
        }

