from django.contrib import admin


from .models import *

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name','price','description',  )
    search_fields = ('name','price', 'description' ,) 
  

@admin.register(StockModel)
class StockModelAdmin(admin.ModelAdmin):
    list_display = ('name','prod','quantity',  )
    search_fields = ('name', 'quantity' ,) 
  