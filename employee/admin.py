from django.contrib import admin
from employee.forms import EmployeeForm
from .models import Employee, InfoPaidSalary


@admin.action(description='delete info_paid')
def delete_info_paid_salary(modeladmin, request, queryset):
    InfoPaidSalary.objects.filter(employee__in=queryset).delete()


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ['__str__', 'view_boss', 'salary', 'all_paid_salary']
    list_filter = ['position', 'position_level']
    actions = [delete_info_paid_salary]


class InfoPaidAdmin(admin.ModelAdmin):
    fields = []
    list_display = ['__str__', 'data_paid', 'paid']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(InfoPaidSalary, InfoPaidAdmin)
