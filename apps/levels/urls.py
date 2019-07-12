from django.conf.urls import url, include
from .api import views
from .api.v2.urls import levels_v2_urls


urlpatterns = [
    url(r'^assesment/', views.pruebas),
    url(r'^towi_index/', views.towi_index),
    url(r'^children/', views.get_children_levels),
    url(r'^create/', views.levels),
    url(r'^connection/', views.connection_reach),
]
