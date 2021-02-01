from django.shortcuts import render
from .models import Product,About_us,Contacts
from .forms import register_form

# Create your views here.
def homepage(request):
    products = Product.objects.all()
    return render(request,'products/products.html',{'products':products})
def us(request):
    about_us=About_us.objects.all()
    return render(request, 'products/about_us.html',{'about_us':about_us})
def cont(request):
    contacts=Contacts.objects.all()
    return render(request,"products/contacts.html",{'contacts':contacts})
def register(request):
    form=register_form
    context={"form":form}
    return render(request,"products/form.html",context)





