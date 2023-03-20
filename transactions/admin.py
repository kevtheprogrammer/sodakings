from django.contrib import admin

from .models import *
 
@admin.register(PurchaseBill)
class PurchaseBillAdmin(admin.ModelAdmin):
    list_display = ('supplier','cgst','sgst','igst', 'cess','tcs' )
    search_fields = ('destination','cgst','sgst',) 
  
@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('billno','stock','quantity','perprice', 'totalprice'  )
    search_fields = ('quantity','perprice', 'totalprice' ,) 
  
  
@admin.register(SaleBill)
class SaleBillAdmin(admin.ModelAdmin):
    list_display = ('customer','destination','sgst','igst', 'cess','tcs' )
    search_fields = ('destination','cgst','sgst',) 
  
@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('billno','stock','quantity','perprice', 'totalprice'  )
    search_fields = ('quantity','perprice', 'totalprice' ,) 
  