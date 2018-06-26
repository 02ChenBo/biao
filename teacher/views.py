from django.shortcuts import render
from teacher.models import Class_room,Student,Student_detail,Teacher
from django.http import HttpResponse
# Create your views here.

def add_1(request):
    class_room=Class_room(
    cls_id=1,
    cname="一班",
    cdata=""
    )
    class_room.save()
    return HttpResponse("添加成功")



def add_2(request):
    student=Student(
    stu_id=2,
    stu_name='老王'
    )
    student.save()
    return HttpResponse("添加成功")


def add_3(request):
    student_detail=Student_detail(
    stu_detail_id=1,
    email='asdasdadad@123132',
    no='123',
    stu_id=1,
    )
    student_detail.save()
    return HttpResponse("添加成功")



def add_4(request):
    teacher=Teacher(
    id=2,
    tea_name="张老师"
    )
    teacher.save()
    return HttpResponse("添加成功")










def update_2(request):
    student=Student.objects.get(stu_id=2)
    student.stu_name="小张"
    student.save()

    return HttpResponse("添加成功")





def find(request):
    teacher=Teacher.objects.all()

    print(teacher)

    return HttpResponse("成功")




from django.db.models import Q
def q_f(request):
    teachers=Teacher.objects.all()
    for teacher in teachers:
        print(teacher.id,teacher.tea_name)
    return HttpResponse("成功")