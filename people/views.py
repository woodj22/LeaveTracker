from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
import sys
import json
from django.core import serializers
from django.views import generic

from .models import Person
# Create your views here.


class IndexView(generic.ListView):
    def get_queryset(self):
        people = Person.objects.all()
        serialized_obj = serializers.serialize('json', people)
        return HttpResponse(serialized_obj, content_type="application/json")


class ShowView(generic.ListView):
    def get_queryset(self):
        try:
            person = Person.objects.get(sam_account_name=account_name)

        except:
            Person.DoesNotExist()
            raise Http404('No person found exception')

        serialized_obj = serializers.serialize('json', [person])
        return HttpResponse(serialized_obj, content_type='application/json')
