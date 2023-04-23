from django.urls import path
from . import views
from .views import Buyer_add_view, Seller_add_view, index

urlpatterns = [
    path("index/",views.index,name='index'),
    path("buyer/add",Buyer_add_view.as_view(),name= 'add-buyer'),
    path("buyer/index",views.buyer_index,name= 'index-buyer'),
    path("buyer/update",views.buyer_update,name= 'update-buyer'),
    path("buyer/view/<int:id>",views.buyer_view,name= 'view-buyer'),
    path("buyer/delete/<int:id>",views.buyer_delete,name= 'delete-buyer'),
    path("buyer/edit/<int:id>",views.buyer_edit,name= 'edit-buyer'),
    path("seller/add",Seller_add_view.as_view(),name= 'add-seller'),
    path("seller/index",views.seller_index,name= 'index-seller'),
    path("seller/update",views.seller_update,name= 'update-seller'),
    path("seller/view/<int:id>",views.seller_view,name= 'view-seller'),
    path("seller/delete/<int:id>",views.seller_delete,name= 'delete-seller'),
    path("seller/edit/<int:id>",views.seller_edit,name= 'edit-seller'),
]