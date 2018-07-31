#-*- coding: utf-8 -*-
#!/usr/bin/python

"""my_blog URL Configuration

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
    2. Add a URL to urlpatterns:  path('my_blog/', include('my_blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from apps.blog import views

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('articles/<int:id>/', views.detail, name='detail'),
    path('category/<int:id>/', views.category, name='category_menu'),
    path('tag/<str:tag>/', views.tag, name='tag_menu'),
    path('archives/<str:year>/<str:month>', views.archives, name='archives'),

    # 此URL用于summernote/upload_attachment 上传接口，
    path('summernote/', include('django_summernote.urls')),


]



# 如果是调试模式，将 url 为 /media/ 开通的 请求，转发到访问 MEDIA_ROOT 文件夹
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [re_path(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns

