from django.urls import path,include
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'product'

urlpatterns = [
    path('',login_required(ProductListView.as_view()),name='listing'),    
    path('add/',login_required(ProductCreateView.as_view()),name='add'),    
    path('stock/',login_required(StockListView.as_view()),name='stock_listing'),    
    path('stock/add/',login_required(StockCreateView.as_view()),name='stock_add'),    
]

 