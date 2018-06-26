from django.db import models

# Create your models here.

class Class_room(models.Model):
    cls_id=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=32,null=False)
    cdata=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='class_room'


class Student(models.Model):
    stu_id=models.AutoField(primary_key=True)
    stu_name=models.CharField(max_length=32,null=False)
    class Meta:
        db_table='student'


class Student_detail(models.Model):
    stu_detail_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=254,null=False)
    no=models.CharField(max_length=128)
    stu_id=models.IntegerField(null=False)
    class Meta:
        db_table='student_detail'


class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    tea_name=models.CharField(max_length=32,null=False)
    class Meta:
        db_table='teacher'

