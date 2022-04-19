from cgitb import html
import email
from random import  randrange
from multiprocessing.connection import Client
from unicodedata import category
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from myapp.models import Product
from .models import *
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest



# Create your views here.
def about(request):
    return render(request,'about.html')
def men(request):
    product = Product.objects.all()
    try:
        cid = Client.objects.get(email=request.session['cemail'])
        return render(request,'men.html',{'cid' : cid,'product' : product})
    except:
        return render(request,'men.html',{'product' : product})
def women(request):
    product = Product.objects.all()
    try:
        cid = Client.objects.get(email=request.session['cemail'])
        return render(request,'women.html',{'cid' : cid,'product' : product})
    except:
        return render(request,'women.html',{'product' : product})

def children(request):
    product = Product.objects.all()
    try:
        cid = Client.objects.get(email=request.session['cemail'])
        return render(request,'children.html',{'cid' : cid,'product' : product})
    except:
        return render(request,'children.html',{'product' : product})

def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def order(request):
    return render(request,'order-complete.html')
def product(request):
    return render(request,'product-detail.html')

def cart(request):
    try:

        cid = Client.objects.get(email=request.session['cemail'])
        book = Booking.objects.filter(client=cid)
        return render(request,'cart.html',{'cid' : cid,'book' : book})
    except:
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
        Client.objects.get(email=request.session['cemail'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                cid = Client.objects.get(email=request.POST['email'])
                if request.POST['password'] == cid.password:
                    request.session['cemail'] = cid.email 
                    return redirect('index')
                return render(request,'clogin.html',{'msg' : 'INCRRECT PASSWORD'})
            except:
                return render(request,'cregister.html',{'msg' : 'EMAIL IS NOT REGISTER PLZ REGISTER EMAIL'})
        return render(request,'clogin.html')
    
def index(request):
    product =Product.objects.all()[::-1]
    if request.method=='POST':
        product=Product.objects.filter(name__contains=request.POST['shoes']),
        product=Product.objects.filter(brand__contains=request.POST['shoes'])
    try:
        cid =Client.objects.get(email=request.session['cemail'])
        return render(request,'index.html',{'cid' : cid,'product':product})
    except:
        return render (request,'index.html',{'product':product})
def clogout(request):
    del request.session['cemail']
    return redirect('index')

def cprofile(request):
    cid =Client.objects.get(email=request.session['cemail'])
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
    cid =Client.objects.get(email=request.session['cemail'])
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
        cid = Client.objects.get(email=request.session['cemail'])
        return render(request,'learn-more.html',{'product':product,'cid':cid})
    except:
        return render(request,'learn-more.html',{'product' : product})

def book_init(request,pk):
    if request.method == 'POST':
        cid = Client.objects.get(email=request.session['cemail'])
        product = Product.objects.get(id=pk)
        book = Booking.objects.create(
            client = cid,
            product = product,
            address = request.POST['address'],
            pay_mode = request.POST['pay'],
            amount = product.price
        )

        if request.POST['pay'] == 'Online':
            currency = 'INR'
            amount = (product.price)*100  # Rs. 200
        
            # Create a Razorpay Order
            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                            currency=currency,
                                                            payment_capture='0'))
        
            # order id of newly created order.
            razorpay_order_id = razorpay_order['id']
            callback_url = f'paymenthandler/{book.id}'
        
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url
            context['book'] =book
            return render(request,'pay.html',context=context)

        else:
            msg = 'Your Booking is confirm you have pay amount onsite.'
            return render(request,'confirm.html',{'cid':cid,'booking':book,'msg':msg})
    try:
        cid = Client.objects.get(email=request.session['cemail'])
        product = Product.objects.get(id=pk)
        return render(request,'book-init.html',{'cid':cid,'product':product})
    except:
        return redirect('client-clogin')
    
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request,pk,pid):
 
    # only accept POST request.
    if request.method == "POST":
        book =Booking.objects.get(id=pk)
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            # if result is None:
            amount = (book.amount)*100 # Rs. 200
            try:

                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
                book.pay_id = payment_id
                book.verify = True
                book.save()

                # render success page on successful caputre of payment
                return render(request, 'success.html')
            except:

                # if there is an error while capturing payment.
                return render(request, 'fail.html')
            # else:
 
            #     # if signature verification fails.
            #     return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()