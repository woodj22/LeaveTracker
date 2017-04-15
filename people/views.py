from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers

from .models import Person
# Create your views here.


def index(request):
    Person.objects.all()
    return HttpResponse("hello this is the people")


def show(request, account_name):

    person = Person.objects.get(sam_account_name=account_name)
    serialized_obj = serializers.serialize('json', [person])
    return HttpResponse(serialized_obj, content_type="application/json")
