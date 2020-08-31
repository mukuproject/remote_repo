from django.shortcuts import render
from testApp.models import Employee,PresentAddress,PermanentAddress,OfficeAddress,EmployeeInfo
from testApp.serializers import EmployeeSerializer,PresentAddressSerializer,PermanentAddressSerializer,OfficeAddressSerializer,EmployeeInfoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
# Create your views here.
class Employee(ModelViewSet):
    #serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    #queryset= Employee.objects.filter(id=id)
    serializer_class=EmployeeSerializer
    #serializer_class=PresentAddressSerializer
class PresentAddress(ModelViewSet):
    serializer_class = PresentAddressSerializer
    queryset = PresentAddress.objects.all()
    #meeting_obj = Meeting.objects.get(pk=pk)
class PermanentAddress(ModelViewSet):
    serializer_class = PermanentAddressSerializer
    queryset = PermanentAddress.objects.all()
class OfficeAddress(ModelViewSet):
    serializer_class = OfficeAddressSerializer
    queryset = OfficeAddress.objects.all()
class EmployeeInfo(ModelViewSet):
    serializer_class = EmployeeInfoSerializer
    queryset = EmployeeInfo.objects.all()
