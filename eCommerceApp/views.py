from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product, UserReview

# Create your views here.


def index(request):
    data = Product.objects.all()[:3]

    value = UserReview.objects.all()[:2]

    return render(request, "index.html", {"datas": data, "values": value})
