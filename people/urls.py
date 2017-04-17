from django.conf.urls import url
from people import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', views.Index)


urlpatterns = [
    url(r'^/$', views.Index.as_view()),
    #url(r'^(?P<account_name>\w{0,50})/$', Show, name='show'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
