from django.urls import path,include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('inventory/', ProductListView.as_view(), name='inventory'),
    path('inventory/update_product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('inventory/delete_product/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
    path('inventory/create_product/', CreateProductView.as_view(), name='create_product'),
    path('inventory/company_details/<int:pk>/', CompanyDetailsView.as_view(), name='company_details'),

]