from django.conf.urls import url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^$', lambda x: HttpResponse('Hello World')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)