from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.views import generic
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from people.serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework import status

from .models import Person


class Index(APIView):

    def get(self, request, format=None):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return HttpResponse(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Show(viewsets.ModelViewSet):
#     def get_queryset(self, account_name):
#         person = get_object_or_404(Person, sam_account_name=account_name)
#         return person
#
#     def get(self, request, account_name):
#         person = self.get_queryset(account_name)
#         serialized_obj = serializers.serialize('json', [person])
#         return HttpResponse(serialized_obj, content_type='application/json')

