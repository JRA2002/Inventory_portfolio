from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'Inventory/product_list.html'
    context_object_name = 'products'

class HomeView(TemplateView):
    template_name = 'Inventory/home.html'
