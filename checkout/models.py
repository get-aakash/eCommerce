from django.db import models
from eCommerceApp.models import Product

# Create your models here.
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    clientFirstName = models.CharField(max_length=255)
    clientLastName = models.CharField(max_length=255)
    clientEmail = models.EmailField()

    def __str__(self):
        return self.clientFirstName
