# Generated by Django 3.1.5 on 2021-01-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('vegan', 'vegan'), ('not_vegan', 'not_vegan')], max_length=40)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('size', models.CharField(choices=[('small', 'small'), ('middle', 'middle'), ('great', 'great')], max_length=20)),
            ],
        ),
    ]
