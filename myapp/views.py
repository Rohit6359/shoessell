from importlib.metadata import files
from django.shortcuts import redirect,render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import  randrange

# from myapp.models import User

# Create your views here.
def aindex(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'aindex.html',{'uid':uid})

def login(request):
    try:
        User.objects.get(email=request.session['email'])
        return redirect('aindex')
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['email'] = uid.email
                    return redirect('aindex')
                return render(request,'page-login.html',{'msg' : 'incrrect password'})
            except:
                return render(request,'page-register.html',{'msg' : 'email is not register plz register your email'})
        return render(request,'page-login.html')

def register(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            return render(request,'page-register.html',{'msg':'email is alrady register'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global temp

                temp = {
                    'name' : request.POST['name'],
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
                return render(request,'otp.html',{'otp':otp})  
            return render(request,'page-register.html',{'msg':'both password is not same '})
    return render(request,'page-register.html')
def otp(request):
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            User.objects.create(
                name = temp['name'],
                email = temp['email'],
                password = temp['password'],
                address = temp['address']

            )
            return render(request,'page-login.html',{'msg' : 'you are sucssesfully register'})
        return render(request,'otp.html',{'otp':request.POST['otp'],'msg':'incorrect otp'})
def logout(request):
    del request.session['email']
    return redirect('login')
def fpassword(request):
    if request.method == 'POST':
        uid=User.objects.get(email=request.POST['email'])
        if uid.email == request.POST['email']:
            otp = randrange(1000,9999)
            subject = 'welcome to Lab App'
            message = f'Your OTP is {otp}. please enter correctly'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'fotp.html',{'otp' : otp,'Email':request.POST['email']})
        return render(request,'forgot_password.html',{'msg':'email is not register'})
    return render(request,'forgot_password.html')
def fotp(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return redirect('aindex')
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email=request.POST['email'])
                if request.POST['password'] == request.POST['otp']:
                    uid.password = request.POST['otp']
                    uid.save()
                    request.session['email']= uid.email
                    return redirect('aindex')
                return render(request,'fotp.html',{'msg' : 'password is incorrect','uid' : uid})
            except:
                return render(request,'fotp.html',{'msg' : 'email is not register---'})
        return render(request,'fotp.html')
def profile(request):
    uid =User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name =request.POST['name']
        uid.email =request.POST['email']
        uid.address =request.POST['address']
        # uid.doj =request.POST['doj'],
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'app-profile.html',{'uid':uid,'msg': 'profile updated'})
    return render(request,'app-profile.html',{'uid':uid})
def chpass(request):
    uid=User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if uid.password == request.POST['opassword']:
            uid.password =request.POST['npassword']
            uid.save()
            return render(request,'chang-password.html',{'msg' : 'PASSWORD IS UPDATED'})
        return render(request,'chang-password.html',{'msg' : 'password is incorrect'})
    return render(request,'chang-password.html')
def add_products(request):
    uid =User.objects.get(email=request.session['email'])
    categories = Category.objects.all()
    if request.method == 'POST':
        cate = Category.objects.get(id=request.POST['pcategory'])
        Product.objects.create(
            seller = uid,
            name = request.POST['pname'],
            brand = request.POST['pbrand'],
            size = request.POST['psize'],
            price = request.POST['pprice'],
            des = request.POST['pdes'],
            category = cate
        )
        msg = 'Service Added'
        return render(request,'add-products.html',{'uid':uid,'categories':categories,'msg':msg})
    return render(request,'add-products.html',{'uid':uid,'categories':categories}) 

def view_my_products(request):
    uid = User.objects.get(email=request.session['email'])
    products = Product.objects.filter(seller=uid)
    return render(request,'view-my-products.html',{'uid' : uid,'products' : products})

def delete_product(request,pk):
    products =Product.objects.get(id=pk)
    products.delete()
    return redirect('view-my-products')

def disable_product(request,pk):
    products =Product.objects.get(id=pk)
    products.available = False
    products.save()
    return redirect('view-my-products')    

def enable_product(request,pk):
    products =Product.objects.get(id=pk)
    products.available = True
    products.save()
    return redirect('view-my-products')    

def view_one_product(request,pk):
    uid = User.objects.get(email=request.session['email'])
    product =Product.objects.get(id=pk)
    return render(request,'view-one-product.html',{'uid':uid,'product': product})

def edit_my_product(request,pk):
    uid = User.objects.get(email=request.session['email'])
    product = Product.objects.get(id=pk)
    cate =Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST['pname']
        product.brand = request.POST['pbrand']
        product.size = request.POST['psize']
        product.price = request.POST['pprice']
        product.category = Category.objects.get(id=request.POST['pcategory'])
        product.des = request.POST['pdes']
        if 'ppic' in request.FILES:
            product.pic =request.FILES['ppic']
        product.save()
        return render(request,'edit-my-product.html',{'product':product,'uid': uid,'cate' : cate ,'msg': '----Product Updated----' })
    return render(request,'edit-my-product.html',{'uid':uid,'cate':cate ,'product':product})





    