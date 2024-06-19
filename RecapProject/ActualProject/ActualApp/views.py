from django.shortcuts import render
from . import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'.templates/ActualApp',context)

