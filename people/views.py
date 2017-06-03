
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from people.serializers import PersonSerializer, ImportDataSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException
import csv
from .models import Person
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
import json
class Index(APIView):
    def get(self, request, format=None):
        people = Person.objects.all()
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(people, request)
        serializer = PersonSerializer(result_page, many=True, context={'data':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImportPeople(APIView):
    def post(self, request):
        import_serializer = ImportDataSerializer(data=request.data)

        if not import_serializer.is_valid():
            return Response('You do not have all the valid keys in the JSON recieved', status=status.HTTP_400_BAD_REQUEST)

        table = request.data.get('tableModel')

        if request.FILES.get('csv'):
            filepath = request.FILES.get('csv')
            csv_dict = csv.DictReader(filepath)

        elif request.data.get('path'):
            filepath = request.data.get('path')
            csv_dict = csv.DictReader(open(filepath))
        try:
            model = ContentType.objects.get(model=table)
        except ObjectDoesNotExist:
            raise TableNotFoundException(incorrect_table_model=table)
        model = apps.get_model(app_label=model.app_label, model_name=table)

        model.addPeopleFromCSV(csv_dict)

        return Response(status=status.HTTP_204_NO_CONTENT)


class RetrievePhoto(APIView):
       def get(self, request):
           return Response('hello from RetrievePhoto')


class TableNotFoundException(APIException):
    def __init__(self, incorrect_table_model):
        super().__init__(detail='the table: '+incorrect_table_model+' has not been found', code='NOT-FOUND_TABLE')
        self.status_code = 400
        self.get_codes()
        self.get_full_details()
