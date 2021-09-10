from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from library.models import Student
from django.shortcuts import render
from library.serializer import StudentSerializer


# Create your views here.
class ListStudentAPIView(ListAPIView):
    """" List all """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudentAPIView(CreateAPIView):
    """ Creations """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateStudentAPIView(UpdateAPIView):
    """ Updating """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudentAPIView(DestroyAPIView):
    """ Deletion """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
