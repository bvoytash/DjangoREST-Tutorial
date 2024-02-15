from rest_framework import serializers
from TestRestProject.Customer.models import Customer, Document, Profession, DataSheet


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ['id', 'description', 'historical_data']


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description', 'status_profession']


class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField()  # should write it with get_.....
    professions = ProfessionSerializer(many=True)
    document_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    data_sheet = DataSheetSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'professions',
                  'status_message', 'data_sheet', 'active', 'num_professions', 'document_set']

    def get_num_professions(self, obj):
        return obj.num_professions()


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'dtype', 'doc_number', 'customer']
