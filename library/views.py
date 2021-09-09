from django.shortcuts import render
from rest_framework import generics
from library.models import Student
from library.serializer import StudentSerializer


# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer
