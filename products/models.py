from django.db import models
from django.shortcuts import  reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_category(cls,category_id):
        return cls.objects.get(id=category_id)


class product(models.Model):
    name =models.CharField(max_length=150)
    image=models.ImageField(upload_to='products/images', null=True ,blank=True)
    description=models.CharField(max_length=200, null=True ,blank=True)
    current_price = models.IntegerField(default=0 ,null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='products')
    email= models.CharField(null=True,max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)


  

    def __str__(self):
      return self.name

    @classmethod
    def get_all_products(cls):
        return  cls.objects.all()

    @classmethod
    def get_specific_product(cls,id):
        return  cls.objects.get(id=id)

    def get_image_url(self):
        return f'/media/{self.image}'

    def get_show_url(self):
        return reverse('products-show',args=[self.id])

    def get_delete_url(self):
        return reverse('products-delete',args=[self.id])

    def get_edit_url(self):
        return reverse('products-edit',args=[self.id])

class User(models.Model):
    user=models.CharField(max_length=50,null=True)
    email= models.CharField(null=True,max_length=100)
    password=models.CharField(max_length=50,null=True)


