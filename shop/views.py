from django.shortcuts import render
from eCommerceApp.models import Product

# Create your views here.


def shop(request):
    data = Product.objects.all()
    return render(request, "shop.html", {"datas": data})
