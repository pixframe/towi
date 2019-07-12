from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth
from django.core.urlresolvers import reverse_lazy
from dashboard.views import *
from suscriptions.webhook import webhook


ccl_urls = [
  url(r'^ccl/$', HomeLaboratorio.as_view(), name='ccl'),
  url(r'^ccl/tools/$', Tools.as_view()),
  url(r'^ccl/data/$', Data.as_view()),
  url(r'^ccl/researchers/$', Researchers.as_view()),
  url(r'^ccl/projects/$', Projects.as_view()),
  url(r'^ccl/resources/$', Resources.as_view()),
  url(r'^ccl/participate/$', Participate.as_view()),
  url(r'^ccl/logout/', auth.logout, {'next_page': '/ccl'}, name='logout-ccl'),
  url(r'^ccl/login/', login_register),
]

urlpatterns = [
    url(r'^inicio/', Login.as_view(), name='login'),
    url(r'^activation-sent/(?P<user_id>\d+)$', ActivateSent.as_view(), name='activation-sent'),
    url(r'^portal/', Home.as_view()),
    url(r'^cuenta/', DataInformation.as_view()),
    url(r'^ninos/', Patients.as_view()),
    url(r'^acerca/', AboutTowi.as_view()),
    url(r'^seguir/', followPatient.as_view()),
    url(r'^evaluacion/(?P<id>\d+)$', AssesmentView.as_view()),
    url(r'^agregar-nino/', AddPatient.as_view()),
    url(r'^registro-nino/', RegisterPatient.as_view()),
    url(r'^vinculaciones/', Invitations.as_view()),
    url(r'^subscripciones', Licencias.as_view()),
    url(r'^validate_email/', email_exists),
    url(r'^validate_coupon/', coupon_exists),
    url(r'^webhook/', webhook),
    url(r'^pruebas/(?P<id>\d+)$', reports_redirect),
    url(r'^get_graph/', get_graph),
    url(r'^asignar-subscripcion/(?P<id>\d+)$', AssignSuscription.as_view(), name='assign-subscription'),  # NOQA
    url(r'^invitar/(?P<id>\d+)$', InviteParent.as_view(), name='invite-parent'),  # NOQA
    url(r'^perfil/(?P<id>\d+)$', EditInfoPacient.as_view(), name='edit-info'),  # NOQA
    url(r'^reportes/(?P<id>\d+)$', Reports.as_view(), name='reports'),  # NOQA
    url(r'^logout/', auth.logout, {'next_page': '/inicio/'}, name='logout'),
    url(r'^grupos/', Groups.as_view()),
    url(
        r'^password_change/$',
        auth.PasswordChangeView.as_view(),
        name='password_change'
    ),
    url(
        r'^password_change/done/$',
        auth.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),
    url(
        r'^recuperar/$',
        CustomPasswordResetView.as_view(
            html_email_template_name='registration/password_reset_html_email.html',
        )
    ),
    url(
        r'^password_reset/done/$',
        auth.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # NOQA
        auth.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(
        r'^reset/done/$',
        auth.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        ActivateAccountView.as_view(), 
        name='activate'
    ),
 ] + ccl_urls
