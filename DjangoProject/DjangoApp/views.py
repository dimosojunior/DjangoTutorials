from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *



# Create your views here.
def homepage(request):
    
    products = Products.objects.all().order_by('-id')
    context = {
        "products":products,
    }
    return render(request, 'DjangoApp/homepage.html', context)

def view_product(request, id):
    products = Products.objects.get(id=id)
    context = {
        "products":products,
    }
    return render(request, 'DjangoApp/view_product.html', context)
def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('homepage')
    
 
def add_product(request):
    form = ProductsForm()
    if request.method == "POST":
        form = ProductsForm(request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context= {
        "form":form
    }
        
    
    
    return render(request, 'DjangoApp/add_product.html', context) 
def update_product(request, id):
    product = Products.objects.get(id=id)
    form = ProductsForm(instance=product)
    if request.method == "POST":
        form = ProductsForm(request.POST, files = request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context= {
        "form":form,
        "product":product
    }
        
    
    
    return render(request, 'DjangoApp/update_product.html', context)  
    

def about(request):
    return render(request, 'DjangoApp/about.html')
