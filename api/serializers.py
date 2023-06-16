
from django.db.models import fields
from rest_framework import serializers
from .models import Employee, Query


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['id', 'date', 'employee', 'employee_name']