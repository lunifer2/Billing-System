from django.urls import path
from . import views
from .views import Item_add_view, item_delete, item_edit, item_update, item_view, item_index
urlpatterns = [
    path('dashboard/',views.seller_dashboard, name='seller-dashboard'),
    path('item/add',Item_add_view.as_view(),name= 'item-add'),
    path('item/index',views.item_index,name= 'item-index'),
    path('item/update',views.item_update,name= 'item-update'),
    path('item/view/<int:id>',views.item_view,name= 'item-view'),
    path('item/delete/<int:id>',views.item_delete,name= 'item-delete'),
    path('item/edit/<int:id>',views.item_edit,name= 'item-edit'),
]