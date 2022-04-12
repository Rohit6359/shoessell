from cgitb import html
import email
from http import client
from random import  randrange
from multiprocessing.connection import Client
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings

from myapp.models import Product
from .models import *



# Create your views here.
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
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            Client.objects.create(
                fname = temp['fname'],
                lname = temp['lname'],
                email = temp['email'],
                password = temp['password'],
                address = temp['address']
            )
            return render(request,'clogin.html',{'msg' : 'you are sucssesfully register'})
        return render(request,'cotp.html',{'otp':request.POST['otp'],'msg':'incorrect otp'})
    return render(request,'cotp.html')

def clogin(request):
    try:
        Client.objects.get(email=request.session['email'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                cid = Client.objects.get(email=request.POST['email'])
                if request.POST['password'] == cid.password:
                    request.session['email'] = cid.email 
                    return redirect('index')
                return render(request,'clogin.html',{'msg' : 'INCRRECT PASSWORD'})
            except:
                return render(request,'cregister.html',{'msg' : 'EMAIL IS NOT REGISTER PLZ REGISTER EMAIL'})
        return render(request,'clogin.html')
    
def index(request):
    product =Product.objects.all()[::-1]
    try:
        cid =Client.objects.get(email=request.session['email'])
        return render(request,'index.html',{'cid' : cid,'product':product})
    except:
        return render (request,'index.html',{'product':product})
def clogout(request):
    del request.session['email']
    return redirect('client-clogin')

def cprofile(request):
    cid =Client.objects.get(email=request.session['email'])
    if request.method == 'POST':
        cid.fname =request.POST['fname']
        cid.lname =request.POST['lname']
        cid.address =request.POST['address']
        # cid.doj =request.POST['doj'],
        if 'pic' in request.FILES:
            cid.pic = request.FILES['pic']
        cid.save()
        return render(request,'cprofile.html',{'cid':cid,'msg': 'profile updated'})
    return render(request,'cprofile.html',{'cid':cid})
def cchangepassword(request):
    cid =Client.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if cid.password == request.POST['opassword']:
            cid.password = request.POST['npassword']
            cid.save()
            return render(request,'changepassword.html',{'cid':cid,'msg':'Password Changed'})
        return render(request,'changepassword.html',{'cid':cid,'msg':'Wrong Password'})
    return render(request,'changepassword.html')

def clearn_more(request,pk):
    product= Product.objects.get(id=pk)
    try:
        cid = Client.objects.get(request.session['email'])
        return render(request,'learn-more.html',{'product':product,'cid':cid})
    except:
        return render(request,'learn-more.html')
        