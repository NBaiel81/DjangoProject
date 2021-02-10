# from django.contrib.auth.models import User
# from django.shortcuts import render
# from .models import Product,About_us,Contacts,Order
# from .forms import *
# User

from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import Product,AboutUs,Contacts
from .forms import *

# Create your views here.
from .token import account_activation_token


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
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            current_site=get_current_site(request)
            mail_subject='Activate your blog account.'
            message = render_to_string('products/acc_active_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email=form.cleaned_data.get('email')
            email=EmailMessage(
                mail_subject,message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete a registration')

    form=SignupForm()
    return render(request,'products/register.html',{'form':form})

def activate(request,uidb64,token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        login(request,user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

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






