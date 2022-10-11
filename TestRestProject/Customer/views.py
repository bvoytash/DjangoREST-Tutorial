from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from TestRestProject.Customer.models import Customer, Document, Profession, DataSheet
from TestRestProject.Customer.serializers import CustomerSerializer, DocumentSerializer, ProfessionSerializer, DataSheetSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True)
    # add a custom behavior. Deactivate customer by /pk/deactivate
    def deactivate(self, request, **kwargs):
        customer = self.get_object()
        customer.active = False
        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    @action(detail=False)
    # activate all customers
    def activate_all(self, request, **kwargs):
        customers = Customer.objects.all()
        customers.update(active=True)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer