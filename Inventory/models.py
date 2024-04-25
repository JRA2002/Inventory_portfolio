from django.db import models

# Create your models here.
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
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self) :
        return self.name