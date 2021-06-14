from django.db import models

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(max_length=255, blank=False)
    clientEmail = models.EmailField(max_length=255, blank=False)
    clientMessage = models.TextField(blank=False)
