from django.contrib import admin
from .models import Product,About_us,Contacts

# Register your models here.
admin.site.register(Product)
admin.site.register(About_us)
admin.site.register(Contacts)