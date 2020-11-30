from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    CONDITION_TYPE = (
        ("new", "New"),
        ("used", "Used"),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="product_images", blank=True, null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image_icon = models.ImageField(upload_to="category_images", blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name
