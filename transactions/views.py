from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView ,View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView , DetailView ,View,TemplateView
from django.contrib.auth.models import Group 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from product.models import NotificationModel

from .models import *
from .forms import *
 

class PurchaseView(TemplateView):
    template_name = "txn/purchase.html"
    form_class = PurchaseBillForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class() 
        context["p_bill"] = PurchaseBill.objects.all() 
        context["p_items"] = PurchaseItem.objects.all() 
        return context

    def post(self,request, **kwargs):
        me = request.user
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(False)
            inst.author = me
            inst.save()
            return redirect('txn:purchase')
        return None 

class PurchaseEditView(CreateView):
    model = PurchaseBill
    form_class = PurchaseItemForm
    template_name = 'txn/p_edit.html'
    
    def get(self,request, pk, **kwargs):
        object = PurchaseBill.objects.get(pk=pk)
        context = {
            "object" :   object,
            "form" :   self.form_class(),
            "p_items" : PurchaseItem.objects.filter(billno=object),
        }
        return render(request,self.template_name,context)
    
    def post(self,request, pk, **kwargs):
        object = PurchaseBill.objects.get(pk=pk)
        me = request.user
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(False)
            inst.maker = me
            inst.billno = object
            inst.save()
            NotificationModel.objects.create(    
                title = "New Stock Added",
                content = f"{me} added a new stock",
                target = me,
            )
            return redirect(object.get_absolute_url())
        return None
    

class SellView(TemplateView):
    template_name = "txn/sell.html"
    form_class = SaleBillForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class() 
        context["s_bill"] = SaleBill.objects.all() 
        context["s_items"] = SaleItem.objects.all() 
        return context

    def post(self,request, **kwargs):
        me = request.user
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(False)
            inst.staff = me
            inst.save()
            return redirect('txn:sales')
        return None 


 
class SellViewEditView(CreateView):
    model = SaleBill
    form_class = SaleItemForm
    template_name = 'txn/s_edit.html'
    
    def get(self,request, pk, **kwargs):
        object = SaleBill.objects.get(pk=pk)
        context = {
            "object" :   object,
            "form" :   self.form_class(),
            "s_items" : SaleItem.objects.filter(billno=object),
        }
        return render(request,self.template_name,context)
    
    def post(self,request, pk, **kwargs):
        object = SaleBill.objects.get(pk=pk)
        me = request.user
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(False)
            # inst.staff = me
            inst.billno = object
            inst.save()
            return redirect(object.get_absolute_url())
        return None