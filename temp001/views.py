from django.shortcuts import render
from temp001.models import User,Teacher,Student
from django.http import HttpResponse

# Create your views here.









def temp_base(request):
    li = ['http://ww1.sinaimg.cn/large/0065oQSqly1frqscr5o00j30k80qzafc.jpg',
          'http://ww1.sinaimg.cn/large/0065oQSqly1frmuto5qlzj30ia0notd8.jpg',
          'http://ww1.sinaimg.cn/large/0065oQSqly1frjd77dt8zj30k80q2aga.jpg',
          ]

    image_dict = {'img1': 'http://ww1.sinaimg.cn/large/0065oQSqly1frjd4var2bj30k80q0dlf.jpg',
                  'img2': 'http://ww1.sinaimg.cn/large/0065oQSqly1frja502w5xj30k80od410.jpg',
                  }

    user = User(img='http://ww1.sinaimg.cn/large/0065oQSqly1fri9zqwzkoj30ql0w3jy0.jpg')

    context = {'name': '小明',
               'age': 1,
               'imgs': li,
               'images': image_dict,
               'user': user,
               }

    return render(request,'temp/temp_base.html',context)




def user_list(request):
    user_dict = User.objects.all()
    return render(request, 'temp/for.html', {'users': user_dict})








def add(request):
    stu1=Student(s_name='刘备',student_id='1')
    stu2 = Student(s_name='关羽', student_id='1')
    stu3 = Student(s_name='张飞', student_id='1')
    stu4 = Student(s_name='赵云', student_id='1')
    stu5 = Student(s_name='诸葛亮', student_id='1')
    stu6 = Student(s_name='黄忠', student_id='1')
    stu7 = Student(s_name='周瑜', student_id='1')
    stu8 = Student(s_name='孙权', student_id='1')
    stu9 = Student(s_name='马超', student_id='1')
    stu10 = Student(s_name='徐庶', student_id='1')
    stu11= Student(s_name='鲁肃', student_id='2')
    stu12= Student(s_name='曹操', student_id='2')
    stu13= Student(s_name='黄盖', student_id='2')
    stu14= Student(s_name='黄忠', student_id='2')
    stu15= Student(s_name='吕布', student_id='2')
    stu16= Student(s_name='貂蝉', student_id='2')
    stu17= Student(s_name='董卓', student_id='2')
    stu18= Student(s_name='庞统', student_id='2')
    stu19= Student(s_name='张郃', student_id='2')
    stu20= Student(s_name='颜良', student_id='2')

    objs=[stu1,stu2,stu3,stu4,stu5,stu6,stu7,stu8,stu9,stu10,
          stu11,stu12,stu13,stu14,stu15,stu16,stu17,stu18,stu19,stu20,]
    Student.objects.bulk_create(objs,batch_size=100)
    return HttpResponse('学生信息添加成功')





def test(request):
    stu_li = Student.objects.all()
    return render(request, 'temp/test.html', {'name':stu_li})



def add1(request):
    if request.method == "GET":
        return render(request, 'temp/add.html')
    elif request.method == 'POST':
        stu_Id = request.POST.get('stu_id')
        stu_Name = request.POST.get('stu_name')
        tea_Id = request.POST.get('tea_id')
        # tea_Name = request.POST.get('tea_name')
        # Teacher.objects.create(t_id=tea_Id,t_name=tea_Name)
        Student.objects.create(s_name=stu_Name,student_id=tea_Id,s_id=stu_Id)
        return HttpResponse("添加成功")






import datetime



def upload(request):
    if request.method=="GET":
        return render(request,'file_upload.html')
    elif request.method=="POST":
        username=request.POST.get('username')
        upload_file=request.FILES.get('head')
        chunks=upload_file.chunks()

        path='media/img/%s'%(get_file_name(upload_file.name))
        with open(path,'wb') as f:
            for chunk in chunks:
                f.write(chunk)
            f.flush()

        return HttpResponse('ok')
    else:
        return HttpResponse('请求不支持')



def get_file_name(old_name):
    # 获取后缀名
    suffix_name = '.' + old_name.split('.')[-1]
    new_name='IMG_%s'%(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    return new_name+suffix_name



#
#
# def test_cookie(request):
#     resp = HttpResponse('测试cookie')
#     msg = request.COOKIES.get('msg')
#     print(msg)
#     if not msg:
#         resp.set_cookie('msg', 'hello', path='/sc/cookie/')
#     return resp
