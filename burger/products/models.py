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

class About_us(models.Model):
    title=models.CharField(max_length=100)
    text1=models.CharField(max_length=500)

