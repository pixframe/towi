from django.conf.urls import url, include
from .webhook import *
from .api.v1 import views

urlpatterns = [
    url(r'^webhook/', webhook),
    url(r'^redeem_code/', views.redeem_coupon),
    url(r'^create/', views.suscription),
    url(r'^children/active/', views.active_child),
    url(r'^children/update/', views.update_user_suscription),
]
