from django.urls import path
from . import views
from .views import buyer_dashboard, Order_add_view, item_view, buyItem, add_order
urlpatterns = [
    path('dashboard/',views.buyer_dashboard, name='buyer-dashboard'),
    path('order/add/<int:id>/',views.add_order, name='order-add'),
    path('item/view/<int:id>/',views.item_view, name='item-view'),
    path('item/order/<int:id>/',views.buyItem, name='order-item'),
]