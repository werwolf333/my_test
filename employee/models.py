from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils.html import format_html


class Employee(models.Model):
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name="name")
    surname = models.CharField(max_length=20, verbose_name="surname")
    patronymic = models.CharField(max_length=20, verbose_name="patronymic")
    position = models.CharField(max_length=20, verbose_name="position")
    boss = models.ForeignKey("self", blank=True, null=True, related_name='workers', on_delete=models.CASCADE)
    employment_date = models.DateField(verbose_name="employment_date")
    salary = models.FloatField(verbose_name="salary")

    def __str__(self):
        return self.position + ': ' + self.surname + ' ' + self.name + ' ' + self.patronymic

    def view_boss(self):
        if self.boss:
            return format_html("<a href=%s/change/>%s</a>" % (self.id, self.boss), self.boss)

    def all_paid_salary(self):
        all_paid = Salary.objects.filter(employee=self).aggregate(Sum('paid'))
        return all_paid['paid__sum']


class Salary(models.Model):
    employee = models.ForeignKey(Employee, related_name='men', on_delete=models.CASCADE)
    data_paid = models.DateField(verbose_name="data_paid")
    paid = models.FloatField(verbose_name="paid", blank=True, null=True)

    def __str__(self):
        return self.employee.__str__()
