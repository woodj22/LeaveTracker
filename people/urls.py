from django.conf.urls import url
from people import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^people/$', views.Index.as_view()),
    url(r'^people/imports/$', views.ImportPeople.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
