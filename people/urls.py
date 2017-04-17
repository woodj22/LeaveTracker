from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<account_name>\w{0,50})/$', views.ShowView.as_view(), name='show'),
]
