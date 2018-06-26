import datetime

from django.shortcuts import render

# Create your views here.

# 缓存的应用
# 全局缓存
# 局部（需要配合模板技术）
# 单视图（在视图函数中使用）

def test_cache(request):
   datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   return render(request,'cache.html',{'time':'time'})