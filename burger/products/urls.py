from django.urls import path
from .views import *#homepage,us,cont,register,user_list,order
urlpatterns=[
    path('products/',homepage),
    path('about_us/',us),
    path('contacts/',cont),
    path('regist/',register),
    path('user_list/',user_list),
    path('order/',order),
    path('create_order/',create_order)
]
