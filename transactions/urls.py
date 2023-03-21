from django.urls import path,include

from .views import *

app_name = 'txn'

urlpatterns = [
    path('',PurchaseView.as_view(),name='purchase'),    
    path('purchase-bill/<int:pk>/edit/',PurchaseEditView.as_view(),name='p_edit'),    
    # path('stock/',StockListView.as_view(),name='stock_listing'),    
    # path('stock/add/',StockCreateView.as_view(),name='stock_add'),    
]

 