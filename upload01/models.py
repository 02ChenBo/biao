from django.db import models

# Create your models here.


class Account(models.Model):
    account_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=64,unique=True,db_index=True)
    password=models.CharField(max_length=128)
    contacts=models.CharField(max_length=64,null=True)
    company=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=11)
    qq=models.CharField(max_length=15)
    head=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

    class Meta:
        db_table='account'