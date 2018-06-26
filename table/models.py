from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=15)
    loc=models.CharField(max_length=50)
    class Meta:
        db_table = 'dept'

class Emp(models.Model):
    empno=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=15)
    job = models.CharField(max_length=10)
    mgr=models.IntegerField()
    hiredate=models.DateTimeField(auto_now=True)
    sal=models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    comm =models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    deptno=models.IntegerField()
    class Meta:
        db_table = 'emp'
