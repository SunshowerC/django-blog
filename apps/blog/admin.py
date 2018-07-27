# -*- coding: utf-8 -*-
# !/usr/bin/python

from django.contrib import admin
from .models import Article, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)  # 给content字段添加富文本



admin.site.register(Article, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)



