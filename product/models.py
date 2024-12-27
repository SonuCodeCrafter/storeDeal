from django.db import models


class Category(models.Model):
    """Represent a Category of Production the store-deal app"""

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text = "Enter the unique the name of the category"
    )

    def __str__(self):
        return self.name




class Product(models.Model):
    """
    Represent a product available in the store deals
    """

    name = models.CharField(
        max_length=255,
        help_text="Enter the name of the product such that(iphone 12, lenovo charger)"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        help_text="Enter the price of the product"
    )
    stock_quantity = models.PositiveIntegerField(help_text="Enter the Quantity of the product")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        help_text="Select the Category of the particular product"
    )
