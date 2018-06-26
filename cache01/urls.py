from django.conf.urls import url
from cache01 import views

urlpatterns = [
    url('cache/', views.test_cache,),

]
