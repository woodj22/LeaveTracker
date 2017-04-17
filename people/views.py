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
from .models import Person
import os


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
        filepath = request.data.get('path')
        with open(filepath) as f:
            reader = csv.reader(f)
            for row in reader:
                Person.objects.get_or_create(
                    sam_account_name=row[0],
                )
        return Response([], status=status.HTTP_204_NO_CONTENT)
