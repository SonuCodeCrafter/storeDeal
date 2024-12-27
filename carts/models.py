from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class CartItem(models.Model):
    """
    Represent an item in a user's shopping carts
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart_item',
        help_text="The User who added this to there shopping cart "
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        help_text="The product that has added to the cart"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        help_text="The number of units of the product is in the cart"
    )

    def __str__(self):
        return f"{self.user.username} ~ {self.product.name} ({self.quantity})"