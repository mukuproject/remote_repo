from django.contrib import admin
from .models import Employee,PresentAddress,PermanentAddress,OfficeAddress,EmployeeInfo
# Register your models here.
admin.site.register(Employee)
admin.site.register(PresentAddress)
admin.site.register(PermanentAddress)
admin.site.register(OfficeAddress)
admin.site.register(EmployeeInfo)
