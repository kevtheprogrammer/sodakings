from django.urls import path,include

from .views import *

app_name = 'product'

urlpatterns = [
    path('',ProductListView.as_view(),name='listing'),    
    path('add/',ProductCreateView.as_view(),name='add'),    
    path('stock/',StockListView.as_view(),name='stock_listing'),    
    path('stock/add/',StockCreateView.as_view(),name='stock_add'),    
]

 