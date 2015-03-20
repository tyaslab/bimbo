from django.conf.urls import url, patterns
from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^$', lambda x: HttpResponse('Hello World')),
)