from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Female'
    GENDER_CHOICES = [
            (MALE, 'Male'),
            (FEMALE, 'Female'),
            (OTHERS, 'Others'),
            ]
    
    BUYER_ROLE = 'Buyer'
    SELLER_ROLE = 'Seller'
    ROLE_CHOICES = [
            (BUYER_ROLE, 'Buyer'),
            (SELLER_ROLE, 'Seller'),
            ]
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    objects = UserManager()
    REQUIRED_FIELDS = []

class Seller(models.Model):
    """ Sellers model """
    seller_name = models.CharField(max_length=50)
    seller_contact = models.IntegerField()
    seller_email = models.EmailField()
    seller_address = models.CharField(max_length=50)
    seller_gender = models.CharField(max_length=10)
    seller_image = models.ImageField(upload_to='Images/Sellers/')
    total_earnings = models.FloatField(default=00.00)
    role = models.CharField(max_length=10,default='Seller',editable=False)

    def __str__(self):
        return self.seller_name
    
    class Meta:
        db_table = "Seller"

class Buyer(models.Model):
    """ Buyers model """
    buyer_name = models.CharField(max_length=50)
    buyer_contact = models.IntegerField()
    buyer_email = models.EmailField()
    buyer_address = models.CharField(max_length=50)
    buyer_gender = models.CharField(max_length=10)
    buyer_image = models.ImageField(upload_to='Images/Sellers/')
    role = models.CharField(max_length=10,default='Buyer', editable=False)

    def __str__(self):
        return self.buyer_name
    
    class Meta:
        db_table = "Buyer"

class PaymentInfo(models.Model):
    """ Stores the credit card info for payment """
    credit_no = models.PositiveIntegerField()
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)


    def __int__(self):
        return self.credit_no

    class Meta:
        db_table = "Payment Info"


class Item(models.Model):
    """ Items Model """
    item_name = models.CharField(max_length=50)
    item_price = models.FloatField(default=00.00)
    item_image = models.ImageField(upload_to='Images/Items/')
    item_description = models.CharField(max_length=250)
    customusers = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.item_name
    
    class Meta:
        db_table = "Items"


class Order(models.Model):
    """ Order Model """
    order_quantity = models.PositiveIntegerField(default=0)
    order_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=10)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_date
    
    class Meta:
        db_table = "Order"


class Bill(models.Model):
    """ Billing Model """
    issue_date = models.DateTimeField(auto_now_add=True)
    paid_date = models.DateTimeField(auto_now_add=True)
    bill_status = models.CharField(max_length=10)
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.bill_status
    
    class Meta:
        db_table = "Bills"

        