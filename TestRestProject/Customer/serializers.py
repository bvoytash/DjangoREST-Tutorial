from rest_framework import serializers

from TestRestProject.Customer.models import Customer, Document, Profession, DataSheet


class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField  # should write it with get_.....

    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'professions',
                  'status_message', 'data_sheet', 'active', 'num_professions']

    def get_num_professions(self, obj):
        return obj.num_professions()


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'dtype', 'doc_number', 'customer']


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description']


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ['id', 'description', 'historical_data']
