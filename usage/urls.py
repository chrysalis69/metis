from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]{4}-[0-9]{2}-[0-9]{2})/([0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.usages),
    url(r'^api/compute/([0-9]{4}-[0-9]{2}-[0-9]{2})/([0-9]{4}-[0-9]{2}-[0-9]{2})/$', api.usages),
    url(r'^api/volumes/$', api.volumes),
    url(r'^api/hypervisor_stats/$', api.hypervisor_stats),
    url(r'^([0-9]{4}-[0-9]{2}-[0-9]{2})/([0-9]{4}-[0-9]{2}-[0-9]{2})/([0-9a-fA-F]{32})/$', views.detail),
    url(r'^api/compute/([0-9]{4}-[0-9]{2}-[0-9]{2})/([0-9]{4}-[0-9]{2}-[0-9]{2})/([0-9a-fA-F]{32})/$', api.detail),
]
