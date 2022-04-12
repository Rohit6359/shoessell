from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('client-about/',views.about,name='client-about'),
    path('client-add/',views.add,name='client-add'),
    path('client-men/',views.men,name='client-men'),
    path('client-cart/',views.cart,name='client-cart'),
    path('client-checkout/',views.checkout,name='client-checkout'),
    path('client-contact/',views.contact,name='client-contact'),
    path('client-order/',views.order,name='client-order'),
    path('client-product/',views.product,name='client-product'),
    path('client-women/',views.women,name='client-women'),
    path('client-clogin/',views.clogin,name='client-clogin'),
    path('client-cregister/',views.cregister,name='client-cregister'),
    path('client-otp/',views.cotp,name='client-otp'),
    path('client-logout/',views.clogout,name='client-logout'),
    path('client-profile/',views.cprofile,name='client-profile'),
    path('client-changepassword/',views.cchangepassword,name='client-changepassword'),
    path('client-learn-more/<int:pk>/',views.clearn_more,name='client-learn-more'),

    





]