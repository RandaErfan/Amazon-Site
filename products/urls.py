from django.urls import path
from .views import show,index,about,contact,delete ,create , edit, login, logout 

urlpatterns=[
    path('<int:product_id>',show,name="products-show"),
    path('',index, name="products-index"),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('<int:product_id>/delete', delete, name='products-delete'),
    path('<int:product_id>/update', edit, name='products-edit'),
    path('create/',create,name='products-create'),
    path('login/',login,name='products-login'),
    path('logout/',logout,name='products-logout'),
    ]