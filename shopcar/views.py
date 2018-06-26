from django.shortcuts import render
from shopcar.models import T_goods_shopcar,Order,Order_goods,User,Goods
from django.http import HttpResponse
# Create your views here.

def add_user(request):
    user1=User(id=1,name='李磊')
    user2=User(id=2,name='张伟')
    user3=User( id=3,name='小红')
    objs=[user1,user2,user3]

    User.objects.bulk_create(objs,batch_size=100)
    return HttpResponse("用户信息添加成功")

def add_goods(request):
    goods1=Goods(id=1,name='牙刷',price='3.5')
    goods2 = Goods(id=2, name='iphone', price='5400')
    goods3 = Goods( id=3,name='毛巾', price='12')
    goods4 = Goods(id=4, name='空调', price='3000')
    goods5 = Goods(id=5, name='电风扇', price='120')
    goods6= Goods(id=6,name='水杯', price='45')
    goods7 = Goods(id=7, name='皮带', price='99')
    objs=[goods1,goods2,goods3,goods4,goods5,goods6,goods7]

    Goods.objects.bulk_create(objs,batch_size=100)
    return HttpResponse('商品添加成功')


def add_order(request):
    # user=User()
    order1=Order(order_number='2018052601',pay_price='',ship_number='111111111',uid_id=1)
    objs=[order1]
    Order.objects.bulk_create(objs,batch_size=100)
    # # Order.objects.create(uid=1,order_number='2018052601',pay_price='',ship_number='111111111')
    return HttpResponse('订单表添加成功')





def add_t_goods_shopcar(request):
    t_goods_shopcar=T_goods_shopcar(num ='123',uid_id=1,goods_id_id=1)
    objs=[t_goods_shopcar]
    T_goods_shopcar.objects.bulk_create(objs,batch_size=100)
    return HttpResponse('添加成功')


# 主表查子表
def find(request):
    user=User.objects.get(pk=1)
    list=user.t_goods_shopcar_set.all()
    for goods_shopcar in list:
        print(goods_shopcar.num)
    return HttpResponse('22')




# 子表查主表
def find1(request):
    shopcar=T_goods_shopcar.objects.get(pk=1)
    print(shopcar.uid.id,shopcar.uid.name)
    return HttpResponse('22')


def find2(request):
    shopcar=T_goods_shopcar.objects.filter(pk=1).first()
    print(shopcar.uid.id,shopcar.uid.name)
    return HttpResponse('22')