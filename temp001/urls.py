from django.conf.urls import url
from temp001 import views

urlpatterns = [
    url('base/',views.temp_base),
    url('add/',views.add),
    url('test/', views.test),
    url('add1/', views.add1),
    # url('upload/', views.upload,name='upload'),
    url('upload/', views.test_cookie),
]
