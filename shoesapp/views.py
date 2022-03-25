from django.shortcuts import render

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