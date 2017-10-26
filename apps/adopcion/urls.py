from django.conf.urls import url
from apps.adopcion.views import index, SolicitudList, SolicitudCreate

urlpatterns = [

    url(r'^$', index),
    url(r'^solicitud/listar$', SolicitudList.as_view(), name= 'solicitud_listar'),
    url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name = 'solicitud_crear')

]
