from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse


# Create your views here.
# views.py

def home(request):
    return render(request,'home.html')

def index(request):
    b=plants.objects.all()
    return render(request,'home.html',{'p':b})

def item_view(request,p):
    b=plants.objects.get(pk=p)
    # n=storess.objects.get(pk=p)
    return render(request,'index.html',{'k':b})

def item_view1(request,p):
    b=storess.objects.get(pk=p)
    return render(request,'index1.html',{'k':b})

def store1(request):
    m=store.objects.all()
    n=storess.objects.all()
    return render(request,'store.html',{'c':m,'f':n})

def item_store(request,c):
    m=store.objects.get(ck=c)
    return render(request,'index.html',{'k':m})


def About_us(request):
    return render(request,'about.html')

def Contact_Us(request):
    return render(request,'contact.html')


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists!!!!!')
                print("already have ")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')         
    return render(request,'signup.html')



def user_login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            request.session['user']=user.username
            return home(request)
        else:
            return HttpResponse("Invalid login details")
    return render(request,'My_account.html')

 
def user_logout(request):
    logout(request)
    return redirect(user_login)

def add_to_cart(request, product_id):
    product = storess.objects.get(pk=product_id)
    # product = store.objects.get(pk=product_id)
    # product = plants.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def remove_item(request,p):
    product = storess.objects.get(pk=p)
    product.delete()
    return redirect(cart)