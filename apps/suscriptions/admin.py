# THIRD PARTY IMPORTS
from import_export.admin import ImportExportModelAdmin

# Django Core Imports
from django.contrib import admin
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


@admin.register(Promos)
class PromosAdmin(ImportExportModelAdmin):
    list_display = ['suscription', 'promo_code', 'unique']
    resource_class = PromoResource


admin.site.register(VerificationCode)
