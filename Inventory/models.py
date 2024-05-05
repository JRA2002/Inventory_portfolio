from django.db import models
from django.db.models import Sum

# Create your models here.
UNITS = {
    ('Kl', 'Kilograms'),
    ('Gr', 'Grams'),
    ('Lt', 'Liters'),
    ('Un', 'Units'),
}
class Company(models.Model):
    name = models.CharField(max_length=20)
    direction = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self) :
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    unit = models.CharField(max_length=2, default='Kg', choices=UNITS)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    due_date = models.DateField(default=None, null=True, blank=True)
    state = models.BooleanField(default=True)

    def __str__(self) :
        return self.name
    
    
    
class Purchase(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return str(self.name)
    
    def total_amount(self):
        return self.quantity * self.name.price
    
    
        
    
    
    
    
    