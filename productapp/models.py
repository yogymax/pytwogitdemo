from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=15)
    pincode=models.IntegerField()
    state=models.CharField(max_length=300)

    class Meta:
        db_table = "Address_Info"


class Customer(models.Model):
    custName = models.CharField(max_length=15)
    custAge = models.IntegerField()
    custBalance = models.IntegerField()

    class Meta:
        db_table = "Customer_Info"


class Product(models.Model):
    productName = models.CharField(max_length=15)
    productPrice=models.IntegerField()
    productQty=models.IntegerField()
    productCat=models.CharField(max_length=300)
    customer=models.ForeignKey(Customer,related_name='products',on_delete=models.CASCADE)
    class Meta:
        db_table = "Product_Info"




class Vendor(models.Model):
    vendorName = models.CharField(max_length=15)
    vendorBalance = models.IntegerField()
    address_id=models.OneToOneField(Address,on_delete=models.CASCADE,related_name='vendor')
    products=models.ManyToManyField(Product,related_name='vendors')
    class Meta:
        db_table = "Vendor_Info"

