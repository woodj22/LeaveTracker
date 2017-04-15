from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<account_name>\w{0,50})/$', views.show, name='show'),
]
