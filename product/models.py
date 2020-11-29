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

    def __str__(self):
        return self.name
