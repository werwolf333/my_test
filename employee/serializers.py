from rest_framework import serializers
from employee.models import Employee, Salary


class EmployeeSerializer(serializers.ModelSerializer):
    info_paid = serializers.SerializerMethodField()

    class Meta:
        fields = ['user', 'name', 'surname', 'patronymic', 'position', 'boss', 'employment_date',
                  'salary', 'info_paid']
        model = Employee

    def get_info_paid(self, obj):
        serializer = Salary.objects.filter(employee=obj)
        return SalarySerializer(serializer, many=True).data


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salary
