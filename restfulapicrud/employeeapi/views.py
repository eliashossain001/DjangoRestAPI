from django.shortcuts import render

from employeeapi.pegination import CustomPagination
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class EmpAPIView(ListCreateAPIView):
    pegination_class= CustomPagination


