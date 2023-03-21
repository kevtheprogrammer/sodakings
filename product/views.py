from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView ,View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView , DetailView ,View,TemplateView
from django.contrib.auth.models import Group 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import *
from .forms import *


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stock_list"] = StockModel.objects.all() 
        return context
    

class ProductListView(ListView):
    model = ProductModel
    template_name = "product/listing.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = ProductModel.objects.all() 
        return context
    
class ProductCreateView(CreateView):
    model = ProductModel
    form_class = ProductForm
    template_name = "product/create.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context
    
    def post(self,request, **kwargs):
        form = self.form_class(self.request.POST,self.request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product:listing')  
          
        return render(request,self.template_name,{'form':form})    
    
class StockListView(ListView):
    model = StockModel
    template_name = "stock/listing.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = StockModel.objects.all() 
        return context
    
    
class StockCreateView(CreateView):
    model = StockModel
    form_class = StockForm
    template_name = "stock/create.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context
    
    def post(self,request, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:stock_listing')  
          
        return render(request,self.template_name,{'form':form})    
    