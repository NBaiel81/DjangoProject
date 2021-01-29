from django.urls import path
from .views import homepage,us,cont
urlpatterns=[
    path('products/',homepage),
    path('about_us/',us),
    path('contacts/',cont)

]