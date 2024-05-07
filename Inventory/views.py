from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product,Company,Purchase
from .forms import ProductForm,PurchaseForm
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request,HttpRequest,JsonResponse
from django.shortcuts import get_object_or_404



# Create your views here.
class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'Inventory/product_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
            
        return context

class HomeView(TemplateView):
    template_name = 'Inventory/home.html'

class UpdateProductView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'Inventory/update_product.html'
    success_url = reverse_lazy('inventory')

    # overriding get_object() means no need to slug_the_url_conf
    def get_object(self, queryset=None):
        name = self.kwargs['name']
        product = get_object_or_404(Product, name=name)
        return product


class DeleteProductView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'Inventory/delete_product.html'
    success_url = reverse_lazy('inventory')

    def get_object(self,queryset=None):
        name = self.kwargs['name']
        product = get_object_or_404(Product, name=name)

        return product

class CreateProductView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'Inventory/create_product.html'
    success_url = reverse_lazy('inventory')

class CompanyDetailsView(LoginRequiredMixin,DetailView):
    model = Company
    template_name = 'Inventory/company_details.html'
    context_object_name = 'company'

    def get_object(self, queryset=None):
        name = self.kwargs['name']
        company = get_object_or_404(Company , name=name)

        return company

class PurchaseListView(LoginRequiredMixin,ListView):
    model = Purchase
    template_name = 'Inventory/purchase_list.html'
    context_object_name = 'purchases'

class CreatePurchaseView(LoginRequiredMixin,CreateView):
    model = Purchase
    template_name = 'Inventory/create_purchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase_list')

class DeletePurchaseView(LoginRequiredMixin,DeleteView):
    model = Purchase
    template_name = 'Inventory/delete_purchase.html'
    success_url = reverse_lazy('purchase_list')

    def get_object(self, queryset: None):
        name = self.kwargs['name']
        purchase = get_object_or_404(Purchase, name=name)
        return purchase

class PurchaseUpdateView(LoginRequiredMixin,UpdateView):
    model = Purchase
    template_name = 'Inventory/update_purchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase_list')

    def get_object(self, queryset: None):
        name = self.kwargs['name']
        purchase = get_object_or_404(Purchase , name__name=name)

        return purchase

def practice_request(request):
    context = {}
    context['home1'] = request.get_full_path()
    context['reponse'] = JsonResponse({"age":"30"})
    return render(request,'Inventory/home1.html',context)

class AboutView(TemplateView):
    template_name = 'Inventory/about.html'

class ProductDetail(DetailView):
    model = Product
    template_name = 'Inventory/product_detail.html'

    

