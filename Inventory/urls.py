from django.urls import path
from Inventory.views import ProductListView,HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('inventory/', ProductListView.as_view(), name='inventory'),

]