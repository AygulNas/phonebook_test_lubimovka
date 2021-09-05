from django.contrib import admin

from .models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'discription',
                    'creator')
    empty_value_display = '-пусто-'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'lastname', 'firstname', 'secondname', 'position',
                    'company', 'phone_number', 'office_number', 'fax_number')
    search_fields = ('company', 'lastname', 'phone_number')
    list_filter = ('company',)
    empty_value_display = '-пусто-'


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
