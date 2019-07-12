from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth
from django.core.urlresolvers import reverse_lazy
from dashboard.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from levels.api.v2.urls import levels_v2_urls


schema_view = get_schema_view(
   openapi.Info(
      title="TOWI API",
      default_version='v1',
      description="This is a REST API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@towi.com.mx"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('dashboard.urls')),
    url(r'^api/', include('accounts.urls')),
    url(r'^api/levels/', include('levels.urls')),
    url(r'^api/v2/levels/', include(levels_v2_urls)),
    url(r'^api/subscription/', include('suscriptions.urls')),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
 ]
