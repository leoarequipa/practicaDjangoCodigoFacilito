from django.conf.urls import url
from django.contrib import admin
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    #url(r'^nuevo$', mascota_view, name='mascota_crear'),
    #url(r'^editar/(?P<id_mascota>\w+)/$', mascota_edit, name='mascota_editar'),
    url(r'^editar/(?P<pk>\w+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\w+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),
    #url(r'^eliminar/(?P<id_mascota>\w+)/$', mascota_delete, name='mascota_eliminar'),

    #vista basada en funciones
    #url(r'^listar$', mascota_list, name='mascota_listar')
    #vista basada en clases
    url(r'^listar$', MascotaList.as_view(), name='mascota_listar')



]
