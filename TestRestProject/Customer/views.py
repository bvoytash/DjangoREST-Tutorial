from django.shortcuts import render
from rest_framework import viewsets

from TestRestProject.Customer.models import Customer
from TestRestProject.Customer.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

