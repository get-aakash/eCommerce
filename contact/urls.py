from django.urls.conf import path
from contact import views


urlpatterns = [
    path("contact", views.contact, name="contact"),
]
