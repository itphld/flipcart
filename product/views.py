from django.shortcuts import render
from .models import Product
from category.models import Category
# Create your views here.
def store(request,category_slug=None):
    if category_slug!=None:
        categories=Category.objects.get(slug=category_slug)
        product=Product.objects.all().filter(is_available=True,category=categories)
        product_count=product.count()
        #product_count=len(product)
    else:


        product=Product.objects.all().filter(is_available=True)
        product_count=product.count()
        #product_count=len(product)
    context={'products': product,
            'product_count':product_count,
    }
    return render(request,'product/store.html',context)


def product_detail(request,product_slug,category_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    context={'single_product':single_product}
    return render(request,'product/product_detail.html',context)
