"""db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings # new
from p2 import views,models
from p2.models import Post, PostImage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>',views.detail_view,name='detail',),
    path('',views.blog_view,name='blog'),



 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
