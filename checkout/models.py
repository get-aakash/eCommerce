from django.db import models

# Create your models here.
class Purchase(models.Model):
    clientFirstName = models.CharField(max_length=255)
    clientLastName = models.CharField(max_length=255)
    clientEmail = models.EmailField()
    purchasedItemName = models.CharField(max_length=255)
    purchasedItemPrice = models.FloatField()
