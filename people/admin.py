from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Person, Leave

admin.site.register(Person)
admin.site.register(Leave)
