from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from library.models import Departments
from library.serializer import DepartmentSerializer


# List your views here.
class ListDepartmentAPIView(ListAPIView):
    """ List all departments """
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


# Create your views here.
class CreateDepartmentAPIView(CreateAPIView):
    """ Creations departments """
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


# Update your views here.
class UpdateDepartmentAPIView(UpdateAPIView):
    """ Updating departments """
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer


# Delete your views here.
class DeleteDepartmentAPIView(DestroyAPIView):
    """ Deletion departments """
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
