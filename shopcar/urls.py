from django.conf.urls import url
from django.contrib import admin
from shopcar import views


urlpatterns = [
    # url('admin/',admin.site.urls),
    url('add_user/',views.add_user),
    url('add_goods/',views.add_goods),
    url('add_order/', views.add_order),
    url('add_t_goods_shopcar/', views.add_t_goods_shopcar),
    url('find/', views.find),
    url('find1/', views.find1),
    url('find2/', views.find2),
]
