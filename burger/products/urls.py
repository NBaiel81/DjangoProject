from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *#homepage,us,cont,register,user_list,order
urlpatterns=[
    path('',homepage,name='home'),
    path('about_us/',us, name="about_us"),
    path('contacts/',cont),
    path('regist/',register, name='register'),
    path('user_list/',user_list,name="users"),
    path('create_order/<int:product_id>/',create_order,name="create_order"),
    path('update_order/<int:order_id>/', update_order),
    path('delete_order/<int:order_id>/', delete_order),
    path('sign_in/',sign_in,name="login"),
    path('logout/',logout_page,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='products/test1.html'),name='reset_password'),
    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name='products/test2.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='products/test3.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='products/test4.html'),name='password_reset_complete'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate')
]

