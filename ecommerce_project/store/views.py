from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product


# Create your views here.
def home(request, category_slug=None):
    category_page= None
    products = None
    if category_slug!=None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page)
    else: 
        products = Product.objects.all().filter(stock=True)
    return render(request,'home.html',{'category':category_page, 'products': products})

def about(request):
    return render(request,'about.html')

def product_page(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html',{'product': product})