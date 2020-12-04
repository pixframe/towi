# THIRD PARTY IMPORTS
from import_export.admin import ImportExportModelAdmin
from django.template.response import TemplateResponse
from django.conf.urls import url
from django.shortcuts import redirect
from django.contrib import admin
# Django Core Imports
from .forms import SuscriptionsFormAdmin
from .models import *
from .resources import PromoResource, SuscriptionResource
from accounts.models import Children


class PromoInline(admin.TabularInline):
    model = Promos
    extra = 0


class SuscriptionInline(admin.TabularInline):
    model = Suscription
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "children":
            if not 'add' in request.path:
                id_ = request.path.split('/')[4]
                kwargs["queryset"] = Children.objects.filter(user__pk=id_)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(SuscriptionType)
class SuscriptionTypeAdmin(admin.ModelAdmin):
    inlines = [PromoInline, ]


@admin.register(Suscription)
class SuscriptionAdmin(ImportExportModelAdmin):
    list_display = ['children', 'id']
    search_fields = ['user__email', ]
    list_filter = ['type', 'is_recurrent', 'trial']
    resource_class = SuscriptionResource
    #change_list_template = 'admin/change_list.html'

    def get_urls(self):
        urls = super(SuscriptionAdmin, self).get_urls()
        my_urls = [
            url(r'^add_suscriptions/$', self.admin_site.admin_view(self.my_view), name='add_suscriptions'),
        ]
        return my_urls + urls

    def my_view(self, request):
        if 'submit' in request.POST:
            form = SuscriptionsFormAdmin(request.POST)
            if form.is_valid():
                user = form.cleaned_data['user']
                type_sub = form.cleaned_data['type_subs']
                subs = form.cleaned_data['suscriptions']
                start_date = form.cleaned_data['init_date']
                finished_date = form.cleaned_data['end_date']
                for _ in range(int(subs)):
                    Suscription.objects.create(
                        user=user,
                        type=type_sub,
                        start_date=start_date,
                        finished_date=finished_date
                    )
                return redirect('/admin/suscriptions/suscription/')
        else:
            form = SuscriptionsFormAdmin()
        context = {
            'form': form,
        }
        return TemplateResponse(request, "admin/preview_template.html", context)

@admin.register(Promos)
class PromosAdmin(ImportExportModelAdmin):
    list_display = ['suscription', 'promo_code', 'unique']
    resource_class = PromoResource


admin.site.register(VerificationCode)
