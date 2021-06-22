from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from eCommerceApp.models import Product
from .forms import StudentForm

# Create your views here.


def shop(request):
    data = Product.objects.all()
    return render(request, "shop.html", {"datas": data})


def show_form_data(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)

        print("this is the post method")
        if fm.is_valid():
            print("the form is validated")

        else:
            print("we arehere")

    else:
        print("this is the get request")
        fm = StudentForm()

    return render(request, "register.html", {"forms": fm})
