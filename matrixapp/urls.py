
from django.urls import path
from .views import*

urlpatterns = [
    path('home/', index),
    path('about/', about),
    path('contact/', contact),
    path('product/', product),
    path('test/', test),
    path('form/', dataget)
]
