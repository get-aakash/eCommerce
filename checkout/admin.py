from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Purchase)


class PostAdmin(admin.ModelAdmin):
    list_display = ["clientFirstName", "clientLastName", "clientEmail", "purchase"]
