from django import forms
from django.core.exceptions import ValidationError
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'user', 'name', 'surname', 'patronymic', 'position', 'boss', 'employment_date',
                  'salary']

    def clean(self):
        pk = self.instance.id
        boss = self.cleaned_data['boss']
        if boss is None:
            if not Employee.objects.filter(boss=None, id=pk).exists():
                if Employee.objects.filter(boss=None).exists():
                    raise ValidationError("there is only one most important boss")
        else:
            if Employee.objects.filter(boss=None, id=pk).exists():
                raise ValidationError("the most important person has no bosses")
            if self.position_level(boss) > 4:
                raise ValidationError("levels only 0 to 4")
            if pk is not None:
                if self.test_loop(boss, Employee.objects.get(id=pk)):
                    raise ValidationError("cannot create a loop")
                else:
                    if (self.position_level(boss) + self.find_staff(Employee.objects.get(id=pk))) > 4:
                        raise ValidationError("you have a large hierarchy of subordinates")

        return self.cleaned_data

    def position_level(self, boss):
        level = 0
        while boss is not None:
            level = level + 1
            boss = boss.boss
        return level

    def test_loop(self, boss, man):
        while boss is not None:
            if boss == man:
                return True
            boss = boss.boss
        return False

    def find_staff(self, boss):
        level = 0
        boss = [boss]
        while Employee.objects.filter(boss__in=boss).exists():
            level = level + 1
            boss = Employee.objects.filter(boss__in=boss)
        return level
