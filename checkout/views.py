from checkout.models import Purchase
from eCommerceApp.models import Product
from django.shortcuts import render


# Create your views here.


def checkout(request):
    return render(request, "checkout.html")


def purchase(request, id):

    data = Product.objects.get(pk=id)

    return render(request, "checkout.html", {"datas": data})


def submit_purchase(request):

    """purchase = Purchase()
    if request.method == "POST":
        purchase.clientFirstName = request.POST["firstName"]
        purchase.clientLastName = request.POST["lastName"]
        purchase.clientEmail = request.POST["email"]
        purchase.purchasedItemName = request.POST.get("productName")
        purchase.purchasedItemPrice = request.POST.get("productPrice")
    purchase.save()
    print("hello")"""
    return render(request, "checkout.html")
