from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Query(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Query {self.id}"
