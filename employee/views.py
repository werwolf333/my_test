from rest_framework.views import APIView
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    message = 'no access to API'

    def has_permission(self, request, view):
        if request.user:
            return request.user.groups.filter(name='level_0').exists()


class AllEmployee(APIView):
    permission_classes = (IsEnrolled,)

    def get(self, request, format=None):
        people = Employee.objects.all()
        people_serializer = EmployeeSerializer(people, many=True)
        return Response(people_serializer.data)


class EmployeeLevel(APIView):
    permission_classes = (IsEnrolled,)

    def get(self, request, level, format=None):
        people = Employee.objects.filter(position_level=level)
        people_serializer = EmployeeSerializer(people, many=True)

        return Response(people_serializer.data)
