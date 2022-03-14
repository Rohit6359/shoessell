from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('profile',views.profile,name='profile'),
    path('calender',views.calender,name='calender'),
    path('chartist',views.chartist,name='chartist'),
    path('chartjs',views.chartjs,name='chartjs'),
    path('flot',views.flot,name='flot'),
    path('morris',views.morris,name='morris'),
    path('peity',views.peity,name='peity'),
    path('sparkline',views.sparkline,name='sparkline'),
    path('compose',views.compose,name='compose'),
    path('inbox',views.inbox,name='inbox'),
    path('read',views.read,name='read'),
    path('summernote',views.summernote,name='summernote'),
    path('element',views.element,name='element'),
    path('pickers',views.pickers,name='pickers'),
    path('validation',views.validation,name='validation'),
    path('wizard',views.wizard,name='wizard'),
    path('index2',views.index2,name='index2'),
    path('layout',views.layout,name='layout'),
    path('jqvmap',views.jqvmap,name='jqvmap'),
    path('error400',views.error400,name='error400'),    
    path('error403',views.error403,name='error403'),
    path('error404',views.error404,name='error404'),
    path('error500',views.error500,name='error500'),    
    path('error503',views.error503,name='error503'),    
    path('lockscreen',views.lockscreen,name='lockscreen'),    
    path('login',views.login,name='login'),
    path('',views.register,name='register'), 
    path('otp',views.otp,name='otp'),    
    path('bootstrap',views.bootstrap,name='bootstrap'),
 
    
    
    
]

