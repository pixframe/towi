# Django Core Libraries
from django.contrib import admin

# THIRD PARTY IMPORTS
from import_export.admin import ImportExportModelAdmin

# Own´s Libraries
from .models import *
from .resources import ChildrenTowiIsalndResource, AverageResource, QuartileResource


class TowiIslandInline(admin.TabularInline):
    model = ChildrenTowiIsland
    extra = 0


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'games', 'order']


@admin.register(ChildrenTowiIsland)
class TowiIslandAdmin(ImportExportModelAdmin):
    list_display = ['parent', 'cid']
    search_fields = ['parent__email', ]
    resource_class = ChildrenTowiIsalndResource


@admin.register(Prueba)
class PruebaAdmin(admin.ModelAdmin):
    list_display = ['header', 'id']


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['parent', 'cid', 'date', 'gamekey', 'id']
    list_filter = ['gamekey', 'date']
    search_fields = ['parent__email', ]


@admin.register(ArbolMusical)
class ArbolAdmin(admin.ModelAdmin):
    list_display = ['header', 'header_date']

    def header_date(self, obj):
        return obj.header.date

    header_date.short_description = 'Fecha'


@admin.register(Average)
class AverageAdmin(ImportExportModelAdmin):
    list_display = ['gender', 'age']
    list_filter = ['gender', 'age']
    resource_class = AverageResource


@admin.register(Quartile)
class QuartileAdmin(ImportExportModelAdmin):
    list_display = ['gender', 'age']
    list_filter = ['gender', 'age']
    resource_class = QuartileResource


admin.site.register(ArbolMusicalV2)
