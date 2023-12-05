from rest_framework import serializers
from customers.models import customer

class custommerSerializer(serializers.ModelSerializer):
  class Meta:
    model = customer
    fields = '__all__'