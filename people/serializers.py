from rest_framework import pagination
from rest_framework import serializers
from people.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('sam_account_name', 'display_name', 'is_manager', 'photo_number')


class PaginatedPersonSerializer(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

    class Meta:
        object_serializer_class = PersonSerializer


class ImportDataSerializer(serializers.Serializer):
    tableModel = serializers.CharField()
    path = serializers.CharField()