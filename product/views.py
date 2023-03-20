from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView ,View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView , DetailView ,View,TemplateView
 
from django.contrib.auth.models import Group 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


class IndexView(TemplateView):
    template_name = "index.html"
