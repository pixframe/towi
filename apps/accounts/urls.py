# DJANGO CORE IMPORTS
from django.conf.urls import url, include

# TOWI IMPORTS
from .api import views


urlpatterns = [
    url(r'^login/', views.login),
    url(r'^profile/sync/', views.sync_profiles),
    url(r'^profile/update/', views.update_profile),
    url(r'^profile/active/', views.active_account),
    url(r'^start_trial/', views.start_trial),
    url(r'^consult_trial/', views.consult_trial),
    url(r'^register/user/', views.register_parent_child),
    url(r'^register/children/', views.register_child),
]
