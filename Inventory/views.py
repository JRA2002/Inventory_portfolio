from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product,Company,Purchase
from .forms import ProductForm,PurchaseForm
from django.db.models import Sum


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'Inventory/product_list.html'
    context_object_name = 'products'

class HomeView(TemplateView):
    template_name = 'Inventory/home.html'

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'Inventory/update_product.html'
    success_url = reverse_lazy('inventory')

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'Inventory/delete_product.html'
    success_url = reverse_lazy('inventory')

class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'Inventory/create_product.html'
    success_url = reverse_lazy('inventory')

class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'Inventory/company_details.html'
    context_object_name = 'company'

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'Inventory/purchase_list.html'
    context_object_name = 'purchases'

class CreatePurchaseView(CreateView):
    model = Purchase
    template_name = 'Inventory/create_purchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase_list')

class DeletePurchaseView(DeleteView):
    model = Purchase
    template_name = 'Inventory/delete_purchase.html'
    success_url = reverse_lazy('purchase_list')

class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = 'Inventory/update_purchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase_list')

    

