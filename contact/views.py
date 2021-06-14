from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Client


# Create your views here.
def contact(request):
    return render(request, "contact.html")


def sample(request):
    return render(request, "sample.html")


def submit_contact(request):

    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["comment"]

    if name == "":
        messages.info(request, "the name field is empty")
        return render(request, "contact.html")
    if email == "":
        messages.info(request, "the email field is empty")
        return render(request, "contact.html")
    if message == "":
        messages.info(request, "the message field is empty")
        return render(request, "contact.html")
    print("this is the submit contact form")
    client_info = Client(clientName=name, clientEmail=email, clientMessage=message)
    client_info.save()
    messages.info(request, "the response has been recorded")
    return render(request, "contact.html")
