from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views import View
from views01.models import User



def base(request):
    return HttpResponse('base')



def list(request,page,size):
    return HttpResponse('当前页数%s 每页%s条'%(page,size))


def list2(request):
    if request.method=='GET':
        page=request.GET.get('page')
        size=request.GET.get('size')
    elif request.method=='POST':
        print('POST')
    return HttpResponse('当前页数%s  每页%s条'%(page,size))




# 访问请求127.0.0.1:8000/views01/login?username=xiaoming&password=123456
def login(request):
    msg=None
    # 判断请求方式  GET，POST必须大写
    if request.method=='GET':
        # 变量名=获取路径中username的值，密码
        username=request.GET.get('username',default='1')
        password=request.GET.get('password')
        # 如果用户输入的用户，密码不为空
        if username and password:
            # 过滤挑选username字段=用户输入的username
            qs=User.objects.first(username=username)
            if len(qs)>0:
                user=qs.first()
                # 根据用户输入的用户名找对应的用户密码判断
                if user.password==password:
                    msg='登录成功'
                else:
                    msg='密码错误'
                pass
            else:
                msg='账号不存在'
        else:
            msg='账号不存在'
    return HttpResponse(msg)




def login1(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        return render(request,'index.html',{'username':username})





