from django.urls import path
from . import views

urlpatterns=[
    path("home/", views.index,name="index"),
    path("pun_img/", views.upload_image,name="citit_img"),
    
]