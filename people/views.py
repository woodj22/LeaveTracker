from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from rest_framework.response import Response

from django.core import serializers
from django.views import generic
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from people.serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework import status
import csv
import codecs
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
        if request.FILES.get('csv'):
            filepath = request.FILES.get('csv')
            csv_dict = csv.DictReader(filepath)

        elif request.data.get('path'):
            filepath = request.data.get('path')
            csv_dict = csv.DictReader(open(filepath))

        Person.addPeopleFromCSV(csv_dict)

        return Response(status=status.HTTP_204_NO_CONTENT)




