from rest_framework import serializers
from .models import *

class AddressSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class CustomerSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VendorSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'