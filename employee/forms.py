from django import forms
from django.core.exceptions import ValidationError
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'user', 'name', 'surname', 'patronymic', 'position', 'position_level', 'boss', 'employment_date',
                  'salary']

    def clean(self):
        pk = self.instance.id
        position_level = self.cleaned_data['position_level']
        boss = self.cleaned_data['boss']
        if 0 > position_level or position_level > 4:
            raise ValidationError("levels only 0 to 4")
        if position_level == 0 and not Employee.objects.filter(position_level=0, id=pk).exists():
            raise ValidationError("there is only one most important boss")
        if boss:
            if boss.position_level == 4:
                raise ValidationError('level 4 cannot be a boss')
            if boss.position_level == position_level:
                raise ValidationError('you can not be on the same level with your boss')
            if abs(boss.position_level - position_level) != 1:
                raise ValidationError('need 1 level difference ')
            if position_level == 0:
                raise ValidationError('the most important person has no bosses ')
        return self.cleaned_data
