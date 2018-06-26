from django.conf.urls import url
from django.contrib import admin
from teacher import views


urlpatterns = [
    # url('admin/',admin.site.urls),
    # url('add_1/',views.add_1),
    # url('add_2/', views.add_2),
    # url('add_3/', views.add_3),
    # url('add_4/', views.add_4),
    # url('update_2/', views.update_2),
    # url('find/', views.find),
    url('q_f/', views.q_f)
]
