from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count, Q



def productlist(request, category_slug=None):
    category = None
    all_products = Product.objects.all().order_by('id')
    categorylist = Category.objects.annotate(total_count=Count('product'))

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        all_products = all_products.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        all_products = all_products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query) |
            Q(category__category_name__icontains=search_query)
        )

    paginator = Paginator(all_products, 5)
    page = request.GET.get('page')
    all_products = paginator.get_page(page)
    template = 'Product/product_list.html'
    context = {'product_list': all_products, 'category_list': categorylist, 'category': category}

    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    detail = Product.objects.get(slug=product_slug)
    images = ProductImages.objects.filter(product=detail)
    template = 'Product/product_detail.html'
    context = {'product_detail': detail, 'product_images': images}
    return render(request, template, context)
