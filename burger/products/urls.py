from django.urls import path
from .views import homepage,us,cont,register
urlpatterns=[
    path('products/',homepage),
    path('about_us/',us),
    path('contacts/',cont),
    path('regist/',register),
]
