from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('men',views.men,name='men'),
    path('add',views.add,name='add'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    path('order',views.order,name='order'),
    path('product',views.product,name='product'),
    path('women',views.women,name='women'),
    path('clogin',views.clogin,name='clogin'),
    path('cregister',views.cregister,name='cregister'),


]