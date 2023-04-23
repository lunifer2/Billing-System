from django.urls import path
from . import views
from .views import Item_add_view
urlpatterns = [
    path('dashboard/',views.seller_dashboard, name='seller-dashboard'),
    path('item/add',Item_add_view.as_view(),name= 'item-add'),
]