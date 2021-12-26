from rest_framework import serializers
from employee.models import Employee, InfoPaidSalary


class EmployeeSerializer(serializers.ModelSerializer):
    info_paid = serializers.SerializerMethodField()

    class Meta:
        fields = ['user', 'name', 'surname', 'patronymic', 'position', 'position_level', 'boss', 'employment_date',
                  'salary', 'info_paid']
        model = Employee

    def get_info_paid(self, obj):
        serializer = InfoPaidSalary.objects.filter(employee=obj)
        return InfoPaidSerializer(serializer, many=True).data


class InfoPaidSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = InfoPaidSalary
