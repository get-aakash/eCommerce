from django.db import models

# Create your models here.
class Product(models.Model):
    productPrice = models.FloatField()
    productName = models.CharField(max_length=255)
    productDescription = models.TextField()
    img = models.ImageField(upload_to="pics")
    awaesome = models.BooleanField(default=False)


class UserReview(models.Model):
    productReview = models.TextField()
    img = models.ImageField(upload_to="reviewPics")
