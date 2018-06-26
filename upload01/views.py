from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse
from upload01.models import Account
from django.views import View
# Create your views here.

import datetime






# 主要函数
def upload(request):
    if request.method=="GET":
        return render(request, 'register.html')
    elif request.method=="POST":
        post(request)
        return HttpResponse('ok')
    else:
        return HttpResponse('请求不支持')



def save_files(request,name):
    head = request.FILES.get(name)
    chunks = head.chunks()
    path = 'media/img/%s' % (get_file_name(head.name))
    with open(path, 'wb') as f:
        for chunk in chunks:
            f.write(chunk)
        f.flush()
    return path


# 获取用户注册上传信息并创建内容到表里面


def post(request):
    password = make_password(request.POST.get('password'))
    email = request.POST.get('email')
    contact=request.POST.get('contact')
    company=request.POST.get('company')
    tel=request.POST.get('tel')
    qq=request.POST.get('qq')
    head=save_files(request,'head')
    try:
        Account.objects.get(email=email)
    except Account.DoesNotExist:
        Account.objects.create(email=email,
                                   password=password,
                                   company=company,
                                   contacts=contact,
                                   phone=tel,
                                   qq=qq,
                                   head=head
                                   )



def get_file_name(old_name):
    # 获取后缀名
    suffix_name = '.' + old_name.split('.')[-1]
    new_name='IMG_%s'%(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    return new_name+suffix_name



#
# class Register(View):
#     def get(self,request):
#         return render(request,'register.html')
#
#     def post(self,request):
#         import hashlib
#         md5=hashlib.md5
#         password=request.POST.get('password')
#
#         password=md5.update(password.encode(encoding='utf-8'))
#         email = request.POST.get('email')
#         contact=request.POST.get('contact')
#         company=request.POST.get('company')
#         tel=request.POST.get('tel')
#         qq=request.POST.get('qq')
#         head=request.FILES.get('head')
#
#         try:
#             Account.objects.get(email=email)
#         except Account.DoesNotExist:
#             Account.objects.create(email=email,
#                                    password=password,
#                                    company=company,
#                                    contacts=contact,
#                                    phone=tel,
#                                    qq=qq,
#                                    head=head
#                                    )
#             return HttpResponse('成功')
#









