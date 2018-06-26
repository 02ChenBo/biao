from django.db import models

# Create your models here.

class T_goods_shopcar(models.Model):
    car_id=models.AutoField(primary_key=True)
    # uid=models.IntegerField()
    # goods_id=models.IntegerField()
    num=models.IntegerField()
    status=models.BooleanField(default=1)
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)

    uid=models.ForeignKey('User',on_delete=models.CASCADE,to_field='id', db_column='u_id')
    goods_id=models.ForeignKey('Goods',on_delete=models.CASCADE,to_field='id', db_column='g_id')
    class Meta:
        db_table='t_goods_shopcar'



class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_number=models.CharField(max_length=50)
    # uid=models.IntegerField()
    pay_price=models.DecimalField(max_digits=20,decimal_places=2)
    is_pay=models.BooleanField(default=0)
    pay_time=models.DateTimeField(auto_now=True)
    is_ship=models.BooleanField(default=0)
    ship_time=models.DateTimeField(auto_now=True)
    is_receipt=models.BooleanField(default=0)
    receipt_time=models.DateTimeField(auto_now=True)
    ship_number=models.CharField(max_length=100)
    status = models.BooleanField(default=1)
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)

    uid=models.ForeignKey('User', on_delete=models.CASCADE, to_field='id', db_column='uid')
    class Meta:
        db_table='order'



class Order_goods(models.Model):
    id=models.IntegerField(primary_key=True)
    # order_id=models.IntegerField()
    # goods_id=models.IntegerField()
    goods_num=models.IntegerField()
    goods_price=models.DecimalField(max_digits=20,decimal_places=2)
    status = models.BooleanField(default=1)
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)

    order_id= models.ForeignKey('Order', on_delete=models.CASCADE, to_field='order_id', db_column='order_id')
    goods_id= models.ForeignKey('Goods', on_delete=models.CASCADE,  to_field='id', db_column='goods_id')
    class Meta:
        db_table='order_goods'




class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    class Meta:
        db_table='user'



class Goods(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    class Meta:
        db_table='goods'