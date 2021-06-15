from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Client


# Create your views here.
def contact(request):
    return render(request, "contact.html")


def sample(request):
    return render(request, "sample.html")


def submit_contact(request):
    client = Client()
    if request.method == "POST":
        client.clientName = request.POST["name"]
        client.clientEmail = request.POST["email"]
        client.clientMessage = request.POST["comment"]

    if client.clientName == "":
        messages.info(request, "the name field is empty")
        return render(request, "contact.html")
    if client.clientEmail == "":
        messages.info(request, "the email field is empty")
        return render(request, "contact.html")
    if client.clientMessage == "":
        messages.info(request, "the message field is empty")
        return render(request, "contact.html")
    print("this is the submit contact form")

    client.save()
    messages.info(request, "the response has been recorded")
    return render(request, "contact.html")
