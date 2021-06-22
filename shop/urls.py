from django.urls.conf import path
from shop import views


urlpatterns = [
    path("shop", views.shop, name="shop"),
    path("userRegister", views.show_form_data, name="userRegister"),
]
