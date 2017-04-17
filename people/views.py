from django.http import HttpResponse, Http404, JsonResponse
from django.core import serializers
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Person
# Create your views here.


class IndexView(generic.ListView):
    def get_queryset(self):
        return Person.objects.all()

    def get(self, request):
        serialized_obj = serializers.serialize('json', self.get_queryset())
        return HttpResponse(serialized_obj, content_type="application/json")


class ShowView(generic.DetailView):
    def get_queryset(self, account_name):
        person = get_object_or_404(Person, sam_account_name= account_name)
        return person

    def get(self, request, account_name):
        person = self.get_queryset(account_name)
        serialized_obj = serializers.serialize('json', [person])
        return HttpResponse(serialized_obj, content_type='application/json')
