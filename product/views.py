from django.shortcuts import render
from .models import Product,ProductImages


def productlist(request):
    all_products = Product.objects.all()

    context = {'product_list': all_products}
    template = 'Product/product_list.html'
    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    detail = Product.objects.get(slug=product_slug)
    images = ProductImages.objects.filter(product=detail)
    template = 'Product/product_detail.html'
    context = {'product_detail': detail, 'product_images': images}
    return render(request, template, context)
