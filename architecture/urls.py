"""architecture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/student/list', views.ListStudentAPIView.as_view(), name="student_list"),
    path('api/v1/student/create', views.CreateStudentAPIView.as_view(), name="student_create"),
    path('api/v1/student/update/<int:pk>', views.UpdateStudentAPIView.as_view(), name="student_update"),
    path('api/v1/student/delete/<int:pk>', views.DeleteStudentAPIView.as_view(), name="student_delete"),
]
