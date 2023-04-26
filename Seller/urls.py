from django.urls import path
from . import views
from .views import Item_add_view, Bill_add_view , create_bill , bill_index , item_delete, item_edit, item_update, item_view, item_index, order_index, order_view
urlpatterns = [
    path('dashboard/',views.seller_dashboard, name='seller-dashboard'),
    path('item/add',Item_add_view.as_view(),name= 'item-add'),
    path('item/index',views.item_index,name= 'item-index'),
    path('item/update',views.item_update,name= 'item-update'),
    path('item/view/<int:id>',views.item_view,name= 'item-view'),
    path('item/delete/<int:id>',views.item_delete,name= 'item-delete'),
    path('item/edit/<int:id>',views.item_edit,name= 'item-edit'),
    path('order/index',views.order_index,name= 'seller-order-index'),
    # path('order/update',views.order_update,name= 'order-update'),
    path('order/view/<int:id>',views.bill_index,name= 'bill-index'),
    # path('order/edit/<int:id>',views.order_edit,name= 'order-edit'),
    # path('bill/index',views.bill_list,name= 'bill-list'),
    path('bill/create/<int:order_id>/',views.create_bill, name= 'bill-create'),
    path('bill/add/<int:order_id>/',Bill_add_view.as_view(),name= 'bill-add'),
]