from testApp.models import Employee,PresentAddress,PermanentAddress,OfficeAddress,EmployeeInfo
from rest_framework.serializers import ModelSerializer
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','employee_first_name','employee_last_name','employee_Date_of_birth','employee_Designation']
        depth=1
class PresentAddressSerializer(ModelSerializer):
    class Meta:
        model=PresentAddress
        fields=['id','employee','Address_line_1','Address_line_2','City','Pin','Country']
        depth=1
class OfficeAddressSerializer(ModelSerializer):
    class Meta:
        model=OfficeAddress
        fields=['id','employee','Address_line_1','Address_line_2','City','Pin','Country']
        depth=1
class PermanentAddressSerializer(ModelSerializer):
    class Meta:
        model=PermanentAddress
        fields=['id','employee','Address_line_1','Address_line_2','City','Pin','Country']
        depth=1
class EmployeeInfoSerializer(ModelSerializer):
    class Meta:
        model=EmployeeInfo
        fields=['id','employee','Address_line_1','Address_line_2','City','Pin','Country']
        depth=1
