from django.db import models
from django.urls import reverse


class ProductModel(models.Model):
    name        = models.CharField(max_length=50)
    thumb       = models.ImageField(upload_to='product/thumb', max_length=None)
    price       = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    updated   = models.DateField( auto_now=True )
    timestamp   = models.DateField( auto_now_add=True )
    slug        = models.SlugField( default=None )

    
    def __str__(self):
        return f'{self.name}' 

    def __unicode__(self):
        return f'{self.name}' 
    
    def get_absolute_url(self):
        return reverse('product:details', args=[self.slug])

class StockModel(models.Model):
    name        = models.CharField(max_length=500)
    prod        = models.ForeignKey(ProductModel, verbose_name="prod", on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    updated   = models.DateField( auto_now=True )
    timestamp   = models.DateField( auto_now_add=True )
    slug        = models.SlugField( default=None )
     
    def get_stock_level(self):
        if self.quantity < 10:
            return 'low'
        elif (self.quantity > 10) and (self.quantity < 50) :
            return 'medium'
        elif self.quantity > 50:
            return 'high'
        
     
    def __str__(self):
        return f'{self.name}' 

    def __unicode__(self):
        return f'{self.name}' 
