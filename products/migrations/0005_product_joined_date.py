# Generated by Django 3.2.20 on 2023-09-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
