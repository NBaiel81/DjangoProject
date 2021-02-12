from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    categories = (
        ('vegan','vegan'),
        ('not_vegan','not_vegan'),
    )
    sizes = (
        ('small','small'),
        ('middle','middle'),
        ('great','great')
    )
    image = models.ImageField(blank=True,null=True,verbose_name='Картинки',default='pizza_default.jpg')
    name = models.CharField(max_length=40,verbose_name='Название',unique=True)
    category = models.CharField(max_length=40,choices=categories,verbose_name='Категория')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')
    price = models.FloatField(verbose_name='Стоимость')
    size = models.CharField(choices=sizes,max_length=50,verbose_name='Размер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class AboutUs(models.Model):
    image =models.ImageField()
    title = models.CharField(max_length=20,verbose_name='Название')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')


    class Meta:
        verbose_name = 'О нас!'
        verbose_name_plural = 'О нас!'


class Contacts(models.Model):
    address = models.CharField(max_length=40,verbose_name='Адрес')
    phone = models.IntegerField(verbose_name='Телефон')
    time = models.CharField(max_length=20,verbose_name='Время')
    mng_name = models.CharField(max_length=40,verbose_name='Имя менеджера')


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Order(models.Model):
    statuses = (
        ('pending','pending'),
        ('in_process','in_process'),
        ('delivered','delivered'),
        ('not_delivered','not_delivered')
    )
    payment_methods = (
        ('Nal', 'Nal'),
        ('Wall', 'Wall')
    )
    payment_type = models.CharField(max_length=20, choices=payment_methods)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=50,choices=statuses,default='in_process',verbose_name='Статус')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Дата')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,verbose_name='Продукты')
    quantity = models.IntegerField(verbose_name='Количество')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Document(models.Model):
    file = models.FileField()

class Profile(models.Model):
    genders = (
        ('Male','Male'),
        ('Female','Female')
    )
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField()
    full_name = models.CharField(max_length=60)
    birth_date = models.DateField(default=date.today())
    phone = models.IntegerField(default=0)
    gender = models.CharField(max_length=20,choices=genders)
    address = models.CharField(max_length=50)
    wallet = models.IntegerField(default=0)
    order_count = models.IntegerField(default=0)







