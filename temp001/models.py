from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=64)




class Teacher(models.Model):
    t_id=models.AutoField(primary_key=True)
    t_name=models.CharField(max_length=32)


class Student(models.Model):
    s_id=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=32)
    student=models.ForeignKey('Teacher',to_field='t_id')