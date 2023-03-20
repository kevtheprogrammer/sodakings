from django.db import models
 
 
from product.models import StockModel
from acc.models import User
 
class PurchaseBill(models.Model):
    supplier = models.ForeignKey(User, on_delete = models.CASCADE, related_name='supplier')
    destination = models.CharField(max_length=50, blank=True, null=True)
    po = models.FileField( upload_to='sales/upload/',blank=True, null=True, max_length=100)
    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    updated   = models.DateField( auto_now=True )
    timestamp   = models.DateField( auto_now_add=True )
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
   
    def __str__(self):
        return "Bill no: " + str(self.pk)
    
    def get_items_list(self):
        return PurchaseItem.objects.filter(pk=self)

    def get_total_price(self):
        purchaseitems = PurchaseItem.objects.filter(pk=self)
        total = 0
        for item in purchaseitems:
            total += item.totalprice
        return total

class PurchaseItem(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(StockModel, on_delete = models.CASCADE, related_name='purchaseitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)
    maker = models.ForeignKey(User, related_name="maker", on_delete=models.CASCADE)

    def __str__(self):
	    return "Bill no: " + str(self.billno.pk) + ", Item = " + self.stock.name

class SaleBill(models.Model):
    customer = models.ForeignKey(User, related_name="customer", on_delete=models.CASCADE)
    gstin = models.CharField(max_length=15)
    destination = models.CharField(max_length=50, blank=True, null=True)   
    po = models.FileField( upload_to='sales/upload/',blank=True, null=True, max_length=100)
    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    staff = models.ForeignKey(User,default=None, related_name="staff", on_delete=models.CASCADE)
    
    def __str__(self):
        return "Bill no: " + str(self.pk)

    def get_items_list(self):
        return SaleItem.objects.filter(pk=self)
        
    def get_total_price(self):
        saleitems = SaleItem.objects.filter(pk=self)
        total = 0
        for item in saleitems:
            total += item.totalprice
        return total

class SaleItem(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete = models.CASCADE, related_name='salebillno')
    stock = models.ForeignKey(StockModel, on_delete = models.CASCADE, related_name='saleitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    def __str__(self):
	    return "Bill no: " + str(self.billno.pk) + ", Item = " + self.stock.name

 
    billno = models.ForeignKey(SaleBill, on_delete = models.CASCADE, related_name='saledetailsbillno') 
    eway = models.CharField(max_length=50, blank=True, null=True)    
    veh = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(default=0)

    def __str__(self):
	    return "Bill no: " + str(self.billno.billno)