from django.db import models

class Employee(models.Model):

    Emp_ID = models.CharField(max_length=100, primary_key=True)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    salary = models.IntegerField()
    dept = models.CharField(max_length=100)

    def __str__(self):
        return self.fname + self.lname

