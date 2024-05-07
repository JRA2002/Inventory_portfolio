from django.urls import path,include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('inventory/', ProductListView.as_view(), name='inventory'),
    path('inventory/update_product/<name>/', UpdateProductView.as_view(), name='update_product'),
    path('inventory/delete_product/<name>/', DeleteProductView.as_view(), name='delete_product'),
    path('inventory/create_product/', CreateProductView.as_view(), name='create_product'),
    path('inventory/company_details/<name>/', CompanyDetailsView.as_view(), name='company_details'),
    path('purchase_list/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchase_list/create_purchase/', CreatePurchaseView.as_view(), name='create_purchase'),
    path('purchase_list/delete_purchase/<name>/', DeletePurchaseView.as_view(), name='delete_purchase'),
    path('purchase_list/update_purchase/<name>/', PurchaseUpdateView.as_view(), name='update_purchase'),
    path('home1/',practice_request,name="home1"),
    path('about/',AboutView.as_view(),name='about'),

]