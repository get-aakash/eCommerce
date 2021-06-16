from django.urls.conf import path
from checkout import views


urlpatterns = [
    path("checkout", views.checkout, name="checkout"),
    path("purchase/<int:id>", views.purchase, name="purchase"),
]
