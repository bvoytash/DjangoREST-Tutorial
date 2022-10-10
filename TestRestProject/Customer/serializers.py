from rest_framework import serializers

from TestRestProject.Customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'professions', 'data_sheet']