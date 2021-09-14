from django.db import models


# Create your models Departments.
class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title


# Create your models Departments.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100, blank=True)


# Create your models Employees.
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100, blank=True)
    Department = models.CharField(max_length=100, blank=True)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
