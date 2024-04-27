from django.contrib import admin
from .models import Product, Company,Purchase

# Register your models here.
#admin.site.register(Product)
admin.site.register(Company)
admin.site .register(Purchase)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','quantity','company','unit','due_date','state']

admin.site.register(Product,ProductAdmin)

