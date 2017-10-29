from django.conf.urls import url
from django.contrib import admin
from apps.mascota.views import listado, index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^editar/(?P<pk>\w+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\w+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    url(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^listado', listado, name="listado")
    #url(r'^nuevo$', mascota_view, name='mascota_crear'),
    #url(r'^editar/(?P<id_mascota>\w+)/$', mascota_edit, name='mascota_editar'),
    #url(r'^eliminar/(?P<id_mascota>\w+)/$', mascota_delete, name='mascota_eliminar'),

    #vista basada en funciones
    #url(r'^listar$', mascota_list, name='mascota_listar')
    #vista basada en clases



]
