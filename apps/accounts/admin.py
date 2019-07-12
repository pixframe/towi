# DJANGO CORE IMPORTS
from django.contrib import admin

# THIRD PARTY IMPORTS
from import_export.admin import ImportExportModelAdmin

# TOWI IMPORTS
from .models import (
    User,
    Children,
    School,
    LinkedAccounts,
    LinkedAccountsChildrens
)
from .resources import ChildrenResource, UserResource
from suscriptions.admin import SuscriptionInline
from levels.admin import TowiIslandInline


admin.site.register(School)


class ChildrenInline(admin.StackedInline):
    model = Children
    extra = 0


class LinkedAccountsChildrensInline(admin.TabularInline):
    model = LinkedAccountsChildrens
    extra = 0


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ['id', 'email', 'user_type']
    inlines = [SuscriptionInline, ChildrenInline]
    search_fields = ['email', ]
    icon = '<i class="material-icons">contacts</i>'
    exclude = ['groups', 'user_permissions']
    resource_class = UserResource

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(obj.password)
        super(UserAdmin, self).save_model(request, obj, form, change)


@admin.register(Children)
class ChildrenAdmin(ImportExportModelAdmin):
    search_fields = ['user__email', ]
    resource_class = ChildrenResource
    inlines = [SuscriptionInline, TowiIslandInline]


@admin.register(LinkedAccounts)
class LinkedAccountsAdmin(admin.ModelAdmin):
    list_display = ['owner_user', 'shared_user']
    search_fields = ['owner_user__email', ]
    inlines = [LinkedAccountsChildrensInline, ]


# @admin.register(LinkedAccountsChildrens)
# class LinkedAccountsChildrensAdmin(admin.ModelAdmin):
#     list_display = ['linked_account', 'cid', 'auth']
#     search_fields = ['cid__user__email', ]
