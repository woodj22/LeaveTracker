from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<account_name>\w{0,50})/$', ShowView.as_view(), name='show'),
]
