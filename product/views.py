from django.shortcuts import render
from .models import Product


def productlist(request):
    all_products = Product.objects.all()

    context = {'product_list': all_products}
    template = 'Product/product_list.html'
    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    detail = Product.objects.get(slug=product_slug)
    template = 'Product/product_detail.html'
    context = {'product_detail': detail}
    return render(request, template, context)
