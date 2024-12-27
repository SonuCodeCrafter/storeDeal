from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import  CartItem
from .serializer import CartItemSerializer
from product.models import Product

class CartItemView(APIView):
    """
    handles viewing and adding item into Cart
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Return all cart item from logged User
        """

        # Add user based logic here
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Add a product to the carts or update its quantity as well
        """

        quantity = request.data.get('quantity')
        product_id = request.data.get('product_id')

        if not product_id:
            return Response({'error':'Product Id is a valid fields'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'},
                            status=status.HTTP_400_BAD_REQUEST)


        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,product=product
        )
        cart_item.quantity = quantity
        cart_item.save()
        message = "Item added to cart" if created else 'cart item updated'
        return Response({
            'message': message
        }, status=status.HTTP_201_CREATED)
