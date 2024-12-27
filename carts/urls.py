from django.urls import path,include
from .views import CartItemView
urlpatterns = [
    path('cart/', CartItemView.as_view(), name='cart')
]