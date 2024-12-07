from django.shortcuts import render
from category.models import Category
from product.models import Product
def home(request):
    product=Product.objects.all().filter(is_available=True)
    context={'products':product}
    return render(request,'home.html',context)
