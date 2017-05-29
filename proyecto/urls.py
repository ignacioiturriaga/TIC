from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from proyecto import views
from proyecto.views import proyectoList, proyectoCreate, proyectoUpdate, proyectoDelete, proyectoDetail, index, proyectoList2, agregar_comentario

urlpatterns = [
    #url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(proyectoCreate.as_view()), name='proyecto_crear'),
    #url(r'^listar$', proyectoList.as_view(), name='proyecto_listar'),
    url(r'^$', proyectoList.as_view(), name='proyecto_listar'),
    url(r'^todos$', proyectoList2.as_view(), name='proyecto_listar0'),
    url(r'^(?P<pk>\d+)$', proyectoDetail.as_view(), name='proyecto_detalle'),
    url(r'^(?P<pk>\d+)/editar$', login_required(proyectoUpdate.as_view()), name='proyecto_editar'),
    url(r'^(?P<pk>\d+)/eliminar/$', login_required(proyectoDelete.as_view()), name='proyecto_eliminar'),
    url(r'^(?P<pk>\d+)/comentar/$', views.agregar_comentario, name='agregar_comentario'),
]