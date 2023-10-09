from django.urls import path
from .views import home,about,contact,show ,delete

urlpatterns=[
    path('',home,name="blog-home"),
    path('about/',about,name="about-us"),
    path('contact/',contact,name="contact-us"),
    path('<int:id>',show,name="blog-show"),  
    path('<int:thing_id>/delete', delete, name='blog-delete'),   


    ]