from django.urls import path,include

from .views import *

app_name = 'txn'

urlpatterns = [
    path('',PurchaseView.as_view(),name='purchase'),    
    path('purchase-bill/<int:pk>/edit/',PurchaseEditView.as_view(),name='p_edit'),    
    path('sales/',SellView.as_view(),name='sales'),    
    path('sales/<int:pk>/add/',SellViewEditView.as_view(),name='s_edit'),    
]

 