from django.db import models
#from testApp.models import Employee,PresentAddress,PermanentAddress,OfficeAddress
# Create your models here.
class Employee(models.Model):
    # presentAddress = models.ForeignKey(PresentAddress, on_delete=models.CASCADE)
    # permanentAddress= models.ForeignKey(PermanentAddress, on_delete=models.CASCADE)
    # officeAddress = models.ForeignKey(OfficeAddress, on_delete=models.CASCADE)
    employee_first_name = models.CharField(max_length=50,null=True)
    employee_last_name = models.CharField(max_length=50,null=True)
    employee_Date_of_birth = models.DateField()
    employee_Designation = models.CharField(max_length=12)
    def __str__(self):
        return self.employee_first_name

class PresentAddress(models.Model):
    # permanentAddress= models.ForeignKey(PermanentAddress, on_delete=models.CASCADE)
    # officeAddress = models.ForeignKey(OfficeAddress, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Address_line_1=models.CharField(max_length=50,null=True)
    Address_line_2=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    Pin=models.IntegerField()
    Country=models.CharField(max_length=50,null=True)
    #permanentAddress= models.ForeignKey(PermanentAddress, on_delete=models.CASCADE)
    def __str__(self):
        return self.Address_line_1
class PermanentAddress(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Address_line_1=models.CharField(max_length=50,null=True)
    Address_line_2=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    Pin=models.IntegerField()
    Country=models.CharField(max_length=50,null=True)
    #presentAddress = models.ForeignKey(PresentAddress, on_delete=models.CASCADE)
    def __str__(self):
        return self.Address_line_1
class OfficeAddress(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Address_line_1=models.CharField(max_length=50,null=True)
    Address_line_2=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    Pin=models.IntegerField()
    Country=models.CharField(max_length=50,null=True)
    #permanentAddress= models.ForeignKey(PermanentAddress, related_name='permanentAddress',on_delete=models.CASCADE)
    #presentAddress = models.ForeignKey(PresentAddress, related_name='presentAddress',on_delete=models.CASCADE)
    def __str__(self):
        return self.Address_line_1
class EmployeeInfo(models.Model):
    #employee_info=models.CharField(max_length=50,null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    presentAddress = models.ForeignKey(PresentAddress, on_delete=models.CASCADE)
    permanentAddress= models.ForeignKey(PermanentAddress, on_delete=models.CASCADE)
    officeAddress = models.ForeignKey(OfficeAddress, on_delete=models.CASCADE)
    
    # Address_line_1=models.CharField(max_length=50,null=True)
    # Address_line_2=models.CharField(max_length=50,null=True)
    # City=models.CharField(max_length=50,null=True)
    # Pin=models.IntegerField()
    # Country=models.CharField(max_length=50,null=True)
    # def __str__(self):
    #     return self.Address_line_1
# class PermanentAddress(EmployeeInfo):
#     pass
# class OfficeAddress(EmployeeInfo):
#     pass
