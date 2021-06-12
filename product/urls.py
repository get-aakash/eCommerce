from django.urls.conf import path
from product import views


urlpatterns = [
    path("product", views.product, name="product"),
]
