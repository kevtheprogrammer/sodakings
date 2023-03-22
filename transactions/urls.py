from django.urls import path,include
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'txn'

urlpatterns = [
    path('',login_required(PurchaseView.as_view()),name='purchase'),    
    path('purchase-bill/<int:pk>/edit/',login_required(PurchaseEditView.as_view()),name='p_edit'),    
    path('sales/',login_required(SellView.as_view()),name='sales'),    
    path('sales/<int:pk>/add/',login_required(SellViewEditView.as_view()),name='s_edit'),    
]

 