from django.contrib import admin
from employee.forms import EmployeeForm
from .models import Employee, Salary


@admin.action(description='delete info_paid')
def delete_info_paid_salary(modeladmin, request, queryset):
    Salary.objects.filter(employee__in=queryset).delete()


class LevelPositionFilter(admin.SimpleListFilter):
    title = ('level')
    parameter_name = 'level'

    def lookups(self, request, model_admin):
        return (
            ('0', ('0')),
            ('1', ('1')),
            ('2', ('2')),
            ('3', ('3')),
            ('4', ('4'))
        )

    def queryset(self, request, queryset):
        if self.value() == '4':
            return Employee.objects.filter(boss__boss__boss__boss__isnull=False, boss__boss__boss__boss__boss__isnull=True)
        if self.value() == '3':
            return Employee.objects.filter(boss__boss__boss__isnull=False, boss__boss__boss__boss__isnull=True)
        if self.value() == '2':
            return Employee.objects.filter(boss__boss__isnull=False, boss__boss__boss__isnull=True)
        if self.value() == '1':
            return Employee.objects.filter(boss__isnull=False, boss__boss__isnull=True)
        if self.value() == '0':
            return Employee.objects.filter(boss__isnull=True)


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ['__str__', 'view_boss', 'salary', 'all_paid_salary']
    list_filter = (LevelPositionFilter, 'position')
    actions = [delete_info_paid_salary]


class InfoPaidAdmin(admin.ModelAdmin):
    fields = []
    list_display = ['__str__', 'data_paid', 'paid']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salary, InfoPaidAdmin)
