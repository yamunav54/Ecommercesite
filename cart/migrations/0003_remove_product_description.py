# Generated by Django 3.0.1 on 2020-06-13 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_product_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]