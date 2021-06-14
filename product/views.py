from django.shortcuts import render
from eCommerceApp.models import Product

# Create your views here.
def product(request):
    data = Product.objects.all()
    for x in data:
        if x.awaesome is True:
            return render(request, "product.html", {"data": x})
