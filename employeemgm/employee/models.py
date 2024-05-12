from django.db import models

class Department(models.Model):
    d_id=models.IntegerField()
    d_name=models.CharField(max_length=50)

    def __str__(self):
        return self.d_name

class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=50)
    emp_age=models.IntegerField()
    emp_address=models.TextField()
    emp_contact_no=models.IntegerField()
    emp_joining_date=models.DateField()
    emp_designation_name=models.CharField(max_length=50)
    d_name=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.emp_id)


