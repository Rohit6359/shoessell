from http import client
from random import  randrange
from multiprocessing.connection import Client
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def index(request):
    return render(request,'index.html') 
def about(request):
    return render(request,'about.html')
def men(request):
    return render(request,'men.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def order(request):
    return render(request,'order-complete.html')
def product(request):
    return render(request,'product-detail.html')
def women(request):
    return render(request,'women.html')
def cart(request):
    return render(request,'cart.html')
def add(request):
    return render(request,'add-to-wishlist.html')
def clogin(request):
    return render(request,'clogin.html')
def cregister(request):
    if request.method == 'POST':
        try:
            Client.objects.get(email=request.POST['email'])
            return render(request,'cregister.html',{'msg':'email is alrady register'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global temp

                temp = {
                    'fname' : request.POST['fname'],
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'password' : request.POST['password'],
                    'address' : request.POST['address']
                }
                otp = randrange(1000,9999)
                subject = 'welcome to scarpa shoes'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail(subject, message, email_from, recipient_list )
                return render(request,'cotp.html',{'otp':otp})  
            return render(request,'cregister.html',{'msg':'both password is not same '})
    return render(request,'cregister.html')
def cotp(request):
    # if request.method == 'POST':
    #     if request.POST['uotp'] == request.POST['otp']:
    #         global temp
    #         Client.objects.create(
    #             fname = temp['fname'],
    #             lname = temp['lname'],
    #             email = temp['email'],
    #             password = temp['password'],
    #             address = temp['address']
    #         )
    #         return render(request,'clogin.html',{'msg' : 'you are sucssesfully register'})
    #     return render(request,'cotp.html',{'otp':request.POST['otp'],'msg':'incorrect otp'})
    return render(request,'cotp.html')

