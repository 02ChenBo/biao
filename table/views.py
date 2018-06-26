from django.shortcuts import render

# Create your views here.
from table.models import Dept,Emp
from django.http import HttpResponse


def add(request):
    table_dept=Dept(
        deptno=1,
    dname="小李",
              loc="222")
    table_dept.save()
    return HttpResponse('添加成功')


def add_emp(request):
    table_emp=Emp(empno=1,
            ename='雍小飞',
            job = "IT",
            mgr=1000,
            sal=10000,
            hiredate='',
            comm =1000,
            deptno=1)
    table_emp.save()
    return HttpResponse('添加成功')

# def delete(request):
#     dept=Dept.objects.get(pk=1,)
#     dept.delete()
#     return HttpResponse('删除成功')

