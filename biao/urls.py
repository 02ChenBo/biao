"""biao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from views01 import views
from temp001 import views
from biao import settings
from django.conf.urls.static import static
urlpatterns = [
    url('admin/', admin.site.urls),
    # url('add/', views.add),
    # url('delete/', views.delete)
    # url('teacher/', include('teacher.urls')),
    # url('shopcar/', include('shopcar.urls'))
    # url(r'^', include('shopcar.urls')),
    # url(r'^', include('views01.urls')),
    url(r'^', include('temp001.urls')),
    url(r'^', include('upload01.urls'))

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
