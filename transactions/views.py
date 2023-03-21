from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView ,View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView , DetailView ,View,TemplateView
from django.contrib.auth.models import Group 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import *
from .forms import *
 

class PurchaseView(TemplateView):
    template_name = "txn/purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["p_bill"] = PurchaseBill.objects.all() 
        context["p_item"] = PurchaseItem.objects.all() 
        return context
    

class PurchaseEditView(CreateView):
    model = PurchaseBill
    form_class = PurchaseBillForm
    template_name = 'txn/p_edit.html'
    
    def get(self,request, pk, **kwargs):
        context = {
            "object" : PurchaseBill.objects.get(pk=pk),
        }
        return render(request,self.template_name,context)
    
    
    