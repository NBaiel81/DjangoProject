from django.db import models

# Create your models here.
class Product(models.Model):
    categories=(
        ('vegan','vegan'),
        ('not_vegan','not_vegan')
    )
    sizes=(
        ('small','small'),
        ('middle','middle'),
        ('great','great')
    )
    name=models.CharField(max_length=40)
    category=models.CharField(max_length=40,choices=categories)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    size=models.CharField(choices=sizes,max_length=20)
    image=models.ImageField(blank=True,null=True)

class About_us(models.Model):
    title=models.CharField(max_length=100)
    text1=models.CharField(max_length=500)

class Contacts(models.Model):
    address=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=50)
    time=models.CharField(max_length=50)
    mng_name=models.CharField(max_length=50)

class Order(models.Model):
    statuses=(
        ('pending','pending'),
        ('in_process','in_process'),
        ('not_delivered',"not_delivered"),
        ('delivered','delivered')
    )
    status=models.CharField(max_length=40,choices=statuses, default='in_process')
    date=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)








