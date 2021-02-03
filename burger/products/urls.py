from django.urls import path
from .views import *#homepage,us,cont,register,user_list,order
urlpatterns=[
    path('products/',homepage,name='home'),
    path('about_us/',us),
    path('contacts/',cont),
    path('regist/',register),
    path('user_list/',user_list),
    path('order/',order),
    path('create_order/',create_order,name="create_order"),
    path('update_order/<int:order_id>/', update_order),
    path('delete_order/<int:order_id>/', delete_order)
]
