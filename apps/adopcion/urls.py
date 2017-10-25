from django.conf.urls import url
from apps.adopcion.views import index, epa
urlpatterns = [

    url(r'^$', index),
    url(r'^coye$', epa)
]
