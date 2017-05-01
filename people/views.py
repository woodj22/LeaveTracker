from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
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
import os
import sys


class Index(APIView):
    def get(self, request, format=None):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImportPeople(APIView):
    def post(self, request):
        serializer = ImportDataSerializer(data=request.data)

        if not serializer.is_valid():
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



class TableNotFoundException(APIException):
    def __init__(self, incorrect_table_model):
        super().__init__(detail='the table: '+incorrect_table_model+' has not been found', code='NOT-FOUND_TABLE')
        self.status_code = 400
        self.get_codes()
        self.get_full_details()
