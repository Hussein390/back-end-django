from customers.models import customer
from django.http import JsonResponse
from customers.serializer import custommerSerializer

def customers(request):
  #invoke serializer and return to client
  data = customer.objects.all()
  serializer = custommerSerializer(data, many=True)
  return JsonResponse({'customers': serializer.data})