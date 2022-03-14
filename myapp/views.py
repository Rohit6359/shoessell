import email
from tempfile import tempdir
from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import random, randrange

from myapp.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')
def profile(request):
    return render(request,'app-profile.html')
def calender(request):
    return render(request,'app-calender.html')
def chartist(request):
    return render(request,'chart-chartist.html')
def chartjs(request):
    return render(request,'chart-chartjs.html')
def flot(request):
    return render(request,'chart-flot.html')
def morris(request):
    return render(request,'chart-morris.html')
def peity(request):
    return render(request,'chart-peity.html')
def sparkline(request):
    return render(request,'chart-sparkline.html')
def compose(request):
    return render(request,'email-compose.html')
def inbox(request):
    return render(request,'email-inbox.html')
def read(request):
    return render(request,'email-read.html')
def summernote(request):
    return render(request,'form-editor-summernote.html')
def element(request):
    return render(request,'form-element.html')
def pickers(request):
    return render(request,'form-pickers.html')
def validation(request):
    return render(request,'form-validation-jquery.html')
def wizard(request):
    return render(request,'form-wizard.html')
def index2(request):
    return render(request,'index2.html')
def layout(request):
    return render(request,'layout-blank.html')
def jqvmap(request):
    return render(request,'map-jqvmap.html')
def error400(request):
    return render(request,'page-error-400.html')
def error403(request):
    return render(request,'page-error-403.html')
def error404(request):
    return render(request,'page-error-404.html')
def error500(request):
    return render(request,'page-error-500.html')
def error503(request):
    return render(request,'page-error-503.html')
def lockscreen(request):
    return render(request,'page-lock-screen.html')
def login(request):
    return render(request,'page-login.html')
def register(request):
    if request.method == 'POST':
        try:
            Register.objects.get(email=request.POST['email'])
            return render(request,'page-register.html',{'msg': 'ENTER EMAIL IS ALREADY REGISTER'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global temp
                
                temp = {     
                     'name' : request.POST['name'],
                     'email' : request.POST['email'],
                     'password' : request.POST['password']
                     }
                otp = randrange(1000,9999)
                subject = 'welcome to Lab App'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'otp.html',{'otp' : otp})
            return render(request,'page-register.html',{'msg':'Both passwords are not matched'})              
    return render(request,'page-register.html')
def otp(request):
    if request.method == 'post':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            Register.objects.create(
                name = temp['name'],
                email =temp['email'],
                password =temp['password']
            )

            msg = "Account is Created"
        return render(request,'login.html',{'msg':msg})
        return render(request,'otp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})                

                
            


    return render(request,'otp.html')
def bootstrap(request):
    return render(request,'table-bootstrap-basic.html')




    