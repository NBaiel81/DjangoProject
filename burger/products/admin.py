from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(AboutUs)
admin.site.register([Contacts,Order])
admin.site.register(Document)

