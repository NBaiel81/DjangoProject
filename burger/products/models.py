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
    category=models.CharField(max_length=40,chices=categories)
    description=models.TextField()
    price=models.FloatField()
    size=models.CharField(choices=sizes,max_length=20)
