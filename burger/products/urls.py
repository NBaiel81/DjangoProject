from django.urls import path
from .views import homepage,us
urlpatterns=[
    path('products/',homepage),
    path('about_us/',us)

]