from django.urls import path
from . import views
urlpatterns = [
    path('aindex',views.aindex,name='aindex'),
    path('profile',views.profile,name='profile'),  
    path('',views.login,name='login'),
    path('register',views.register,name='register'), 
    path('logout',views.logout,name='logout'), 
    path('otp',views.otp,name='otp'),
    path('fpassword',views.fpassword,name='fpassword'),   
    path('fotp',views.fotp,name='fotp'),   
    path('chpass',views.chpass,name='chpass'),
    path('add-products',views.add_products,name='add-products'),
    path('view-my-products',views.view_my_products,name='view-my-products'),
    path('delete-product/<int:pk>',views.delete_product,name='delete-product'),
    path('disable-product/<int:pk>',views.disable_product,name='disable-product'),
    path('enable-product/<int:pk>',views.enable_product,name='enable-product'),
    path('view-one-product/<int:pk>',views.view_one_product,name='view-one-product'),
    path('edit-my-product/<int:pk>',views.edit_my_product,name='edit-my-product'),
    path('view-clients-orders',views.view_clients_order,name='view-clients-orders'),





    
 
    
    
    
]

