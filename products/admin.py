from django.contrib import admin

# Register your models here.
from products.models import product ,Category,User

admin.site.register(product)
admin.site.register(Category)
admin.site.register(User)