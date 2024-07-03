from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
    def _str_(self):
        return self.name

class Bike(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to="bike_images",default="default.jpg",null=True,blank=True)
    category_object=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="item")
    Model_year=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    km=models.PositiveBigIntegerField()
    is_placed=models.BooleanField(default=False)
    
      
    def _str_(self):
        return self.title
    


    
    
    

class Order(models.Model):

    user_object=models.ForeignKey(User,on_delete=models.CASCADE,related_name="purchase")
    Bike_object=models.ForeignKey(Bike,on_delete=models.CASCADE,related_name="bike")
    delivery_address=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=200,null=True)
    is_paid=models.BooleanField(default=False)
    total=models.PositiveIntegerField()
    order_id=models.CharField(max_length=200,null=True)
    created_date=models.DateTimeField(auto_now_add=True ,null=True)


    options=(
        ("cod","cod"),
        ("online","online")
    )
    payment=models.CharField(max_length=200,choices=options,default="cod")
    option=(
        ("order-placed","order-placed"),
        ("intransit","intransit"),
        ("dispatched","dispatched"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=option,default="order-placed")
     
    @property
    def orderstatus(self):
        if self.status=="order-placed":
            placed=True
            return placed
    @property
    def orderstatus1(self):
        if self.status=="intransit":
            shipped=True
            return shipped
    

        

class PriceRange(models.Model):
    range=models.PositiveIntegerField()
   




class Service(models.Model):
    name=models.CharField(max_length=200)
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="repair")
    date=models.DateTimeField()
    description=models.CharField(max_length=200)
    serviced=models.BooleanField(default=False)
    comment=models.CharField(max_length=200)
    
    
    def _str_(self):
        return self.name
    @property
    def status(self):
        if self.serviced==True:
            return "Completed"
        else:
            return "pending"
        




