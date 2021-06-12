from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    data = Product.objects.all()

    return render(request, "index.html", {"datas": data})