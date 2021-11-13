from django.db import models
import datetime as dt
from django.urls import reverse
from url_or_relative_url_field.fields import URLOrRelativeURLField

# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{ self.name }"

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField('image')
    link = URLOrRelativeURLField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', null=True)
    users = models.ManyToManyField(User, through='Cart')

    def __str__(self):
        return f"{ self.title }"

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.pk})




# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField('image')
    contact = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"CartID : { self.pk }"

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.pk})        