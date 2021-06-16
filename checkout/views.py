from django.http.response import HttpResponse
from checkout.models import Purchase
from eCommerceApp.models import Product
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.


def checkout(request):
    return render(request, "checkout.html")


def purchase(request, id):
    print(id)
    purchase = Purchase()
    data = Product.objects.get(pk=id)

    if request.method == "POST":

        purchase.clientFirstName = request.POST["firstName"]
        purchase.clientLastName = request.POST["lastName"]
        purchase.clientEmail = request.POST["email"]
        purchase.purchasedItemName = data.productName
        purchase.purchasedItemPrice = data.productPrice
        if purchase.clientLastName == "":
            messages.info(request, "the lastName field is empty")
            return render(request, "checkout.html")
        if purchase.clientEmail == "":
            messages.info(request, "the email field is empty")
            return render(request, "checkout.html")
        purchase.save()
        messages.info(request, "the purchase is successful")
        return render(request, "checkout.html")

    return render(request, "checkout.html", {"datas": data})
