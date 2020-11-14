from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    profile_pic = models.CharField(max_length=300, default="")
    mobile_no = models.CharField(max_length=10, default="0")
    street = models.CharField(max_length=700, default="")
    city = models.CharField(max_length=700, default="")
    state = models.CharField(max_length=700, default="")
    country = models.CharField(max_length=700, default="")
    freelancer = models.BooleanField(default=False)
    seller = models.BooleanField(default=False)

class Freelancer(models.Model):
    fl_id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(to=Profile, related_name='user_freelancer_set', on_delete=CASCADE)
    fl_address = models.TextField(blank=False, default="", max_length=700)
    fl_skills = models.CharField(max_length=250, default="")
    fl_experience = models.IntegerField()
    fl_education = models.CharField(max_length=250, default="")

class Seller(models.Model):
    sl_id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(to=Profile, related_name='user_seller_set', on_delete=CASCADE)
    company_name = models.CharField(max_length=300, default="")
    sl_address = models.TextField(blank=False, default="", max_length=700)

class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True, auto_created=True)
    sold_by = models.ForeignKey(to=Seller, on_delete=CASCADE)
    prod_name = models.CharField(max_length=250, default="")
    prod_pic = models.ImageField(upload_to='EngineeringDeal/products')
    prod_category = models.CharField(max_length=300, default="")
    prod_description = models.TextField(max_length=700, default="")
    prod_instruction = models.TextField(max_length=700, default="")
    prod_available = models.BooleanField(default=True)
    prod_price = models.IntegerField(default=0)


class Order(models.Model):
    ordered_by = models.ForeignKey(to=Profile, on_delete=CASCADE)
    product = models.ForeignKey(to=Product, on_delete=CASCADE)
    order_status = models.CharField(max_length=250, default="") # pending, wishlisted, done , completed
    ordered_date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_label = models.CharField(unique=True, max_length=200, default="")

class Skills(models.Model):
    sk_id = models.IntegerField(primary_key=True)
    sk_label = models.CharField(unique=True, max_length=200, default="")

class HireFreelancer(models.Model):
    hired_by = models.ForeignKey(to=Profile, related_name='hired_by_hireFreelancer_set', on_delete=CASCADE)
    hired_to = models.ForeignKey(to=Profile, related_name='hired_to_hireFreelancer_set', on_delete=CASCADE)




