from django.urls import path
from . import views
from .views import buyer_dashboard , Order_add_view, item_view, buyItem, add_order, order_index, bill_index, payment_create
urlpatterns = [
    path('dashboard/',views.buyer_dashboard, name='buyer-dashboard'),
    path('order/add/<int:id>/',views.add_order, name='order-add'),
    path('item/view/<int:id>/',views.item_view, name='item-view'),
    path('item/order/<int:id>/',views.buyItem, name='order-item'),
    path('order/index',views.order_index,name= 'order-index'),
    path('payment/<int:bill_id>/create/',views.payment_create,name= 'payment-create'),
    path('bill/view/<int:id>',views.bill_index,name= 'buyer-bill-index'),
]