from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import ProfileUpdate, ProfileDetail

urlpatterns = [
    #url(r'perfil/(?P<username>[a-zA-Z0-9]+)$', ProfileDetail.as_view(), name='perfil'),
    url(r'^(?P<pk>\d+)/editar$', login_required(ProfileUpdate.as_view()), name='profile_editar'),
]
