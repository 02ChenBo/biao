from django.conf.urls import url
from upload01 import views

urlpatterns = [
    url('upload01/', views.upload,name='upload'),

]
