from django.db import models

# Create your models here.

class User(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=32,db_column=True,unique=True)
    password=models.CharField(max_length=32)
    status=models.IntegerField(default=1)

    class Meta:
        db_table='t_user'