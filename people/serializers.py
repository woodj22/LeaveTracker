from rest_framework import pagination
from rest_framework import serializers
from people.models import Person



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('sam_account_name', 'display_name', 'is_manager', 'photo_number')


class ImportDataSerializer(serializers.Serializer):
    tableModel = serializers.CharField()
    path = serializers.CharField()
