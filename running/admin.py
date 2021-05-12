from django.contrib import admin
from .models import Country, Province, Area, City


class ReadOnlyAdmin(admin.ModelAdmin):
    """
    • 集成遗留的已有系统
    • 已有系统的数据涉及到核心数据
    • 为了确保数据安全，管理后台只提供数据的浏览功能
    • 设置列表页list_display展示所有字段
    """

    readonly_fields = []

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Country)
class CountryAdmin(ReadOnlyAdmin):
    search_fields = ('chn_name', 'eng_name',)


@admin.register(Province)
class ProvinceAdmin(ReadOnlyAdmin):
    search_fields = ('chn_name', 'eng_name',)


@admin.register(City)
class CityAdmin(ReadOnlyAdmin):
    autocomplete_fields = ['provinceid', 'countryid', ]

    list_display = ('cityid', 'countryid', 'areaid', 'provinceid', 'chn_name', 'eng_name')
