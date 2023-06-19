from rest_framework.test import APITestCase
from api.models import Employee, Query
from rest_framework import status

class EmployeeTestCase(APITestCase):
    def setUp(self):
        Employee.objects.create(name="jhon")
        Employee.objects.create(name="marie")
        Employee.objects.create(name="edward")

        self.employees = Employee.objects.all()

    def test_get_all_employees(self):
        self.assertEqual(self.employees.count(), 3)
        response = self.client.get('/employee/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_employee(self):
        for employee in self.employees:
            response = self.client.get(f'/employee/{employee.id}/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        data = {'name': 'Alice'}
        response = self.client.post('/employee/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_employee(self):
        employee = Employee.objects.create(name='Edward')
        data = {'name': 'Edward Smith'}
        response = self.client.put(f'/employee/update/{employee.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_employee = Employee.objects.get(id=employee.id)
        self.assertEqual(updated_employee.name, 'Edward Smith')

    def test_delete_employee(self):
        employee = Employee.objects.create(name='Jhon')
        response = self.client.delete(f'/employee/{employee.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
    
class QueryTestCase(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name='John')
        self.query1 = Query.objects.create(date="2023-06-01", employee=self.employee, employee_name="Jhon Doe")
        self.query2 = Query.objects.create(date="2023-06-02", employee=self.employee, employee_name="Jhon Smith")

    def test_get_all_queries(self):
        response = self.client.get('/query/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_query_by_employee_name(self):
        name = {'employee_name': 'Jhon Doe'}
        response = self.client.post('/query/consult/', data=name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

            