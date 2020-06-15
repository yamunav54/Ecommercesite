# Generated by Django 3.0.1 on 2020-06-13 10:19

import cart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200613_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to=cart.models.directory),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.TextField(),
        ),
    ]
