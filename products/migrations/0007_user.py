# Generated by Django 3.2.20 on 2023-09-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20230930_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('password', models.IntegerField(max_length=50, null=True)),
            ],
        ),
    ]
