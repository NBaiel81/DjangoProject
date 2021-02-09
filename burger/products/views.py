# from django.contrib.auth.models import User
# from django.shortcuts import render
# from .models import Product,About_us,Contacts,Order
# from .forms import *
# User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Product,AboutUs,Contacts
from .forms import *

# Create your views here.
def homepage(request):
    products = Product.objects.all()
    return render(request,'products/products.html',{'products':products})
def us(request):
    about_us=AboutUs.objects.all()
    return render(request, 'products/about_us.html',{'about_us':about_us})
def cont(request):
    contacts=Contacts.objects.all()
    return render(request,"products/contacts.html",{'contacts':contacts})
def register(request):
    form=UserCreationForm
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={"form":form}
    return render(request,"products/register.html",context)

def user_list(request):
    users=User.objects.all()
    return render(request,"products/user_list.html",{'users':users})

def order(request):
    orders=Order.objects.all()
    return render(request,"products/order.html",{"orders":orders})

def create_order(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'products/create_order.html',context)

def update_order(request,order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'products/create_order.html',context)

def delete_order(request,order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {'order':order}
    return render(request,'products/delete.html',context)

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request,'products/login.html')

def logout_page(register):
    logout(register)
    return redirect('home')





