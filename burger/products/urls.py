from django.urls import path
from .views import *#homepage,us,cont,register,user_list,order
urlpatterns=[
    path('products/',homepage,name='home'),
    path('about_us/',us, name="about_us"),
    path('contacts/',cont),
    path('regist/',register, name='register'),
    path('user_list/',user_list,name="users"),
    path('order/',order,name='create_order'),
    path('create_order/',create_order,name="create_order"),
    path('update_order/<int:order_id>/', update_order),
    path('delete_order/<int:order_id>/', delete_order),
    path('sign_in/',sign_in,name="login")
]

