from django.urls import path
from . import views
from .views import buyer_dashboard, Order_add_view, item_view
urlpatterns = [
    path('dashboard/',views.buyer_dashboard, name='buyer-dashboard'),
    path('order/add/',Order_add_view.as_view(), name='order-item'),
    path('item/view/<int:id>/',views.item_view, name='item-view')
]