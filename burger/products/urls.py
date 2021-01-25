from django.urls import path
from .views import homepage
urlpatterns=[
    path('products/',homepage)
]