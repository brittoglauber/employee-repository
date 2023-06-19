from django.shortcuts import get_object_or_404, render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Query
from .serializers import EmployeeSerializer, QuerySerializer

from rest_framework import serializers
from rest_framework import status
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Name': '/?category=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)


@api_view(['POST'])
def add_employee(request):
    employee = EmployeeSerializer(data=request.data)

    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This user already exists!')
    
    if employee.is_valid():
        employee.save()
        return Response(employee.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_employee(request):
    if request.query_params:
        employee = Employee.objects.filter(**request.query_param.dict())
    else:
        employee = Employee.objects.all()

    if employee:
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_employee_byId(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    

@api_view(['PUT'])
def update_employee(request, pk):
    employee = employee = Employee.objects.get(pk=pk)
    data = EmployeeSerializer(instance=employee, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def add_query(request):
    employee_name = request.data.get('employee_name')

    try:
        employee = Employee.objects.get(name=employee_name)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    query_data = {
        'date': request.data.get('date'),
        'employee': employee.id,
        'employee_name': employee_name
    }

    query_serializer = QuerySerializer(data=query_data)

    if query_serializer.is_valid():
        query_serializer.save()
        return Response(query_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(query_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def view_query(request):
    if request.query_params:
        query = Query.objects.filter(**request.query_param.dict())
    else:
        query = Query.objects.all()
        

    if query:
        serializer = QuerySerializer(query, many=True)
        return Response(serializer.data)
    else:
        return Response(data='Query not founded!', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def search_query_by_employee_name(request):
    employee_name = request.data.get('employee_name')
    
    if not employee_name:
        return Response({'error': 'employee_name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    queries = Query.objects.filter(employee_name__icontains=employee_name)
    serializer = QuerySerializer(queries, many=True)
    return Response(serializer.data)

def home(request):
    return render(request, 'employees/home.html')

# def employees(request):
#     new_employee = Employee()
#     new_employee.name = request.POST.get('name')
#     new_employee.save()

#     employees = {
#         'employees': Employee.objects.all()
#     }

#     return render(request, 'employees/employee.html', employees)


def employees(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Verificar se o usuário já existe no banco de dados
        existing_employee = Employee.objects.filter(name=name).exists()

        if existing_employee:
            return HttpResponse("Usuário já existe no banco de dados!")

        # Criar um novo funcionário
        new_employee = Employee()
        new_employee.name = name
        new_employee.save()

    employees = {
        'employees': Employee.objects.all()
    }

    return render(request, 'employees/employee.html', employees)