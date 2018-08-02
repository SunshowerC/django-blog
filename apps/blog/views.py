#-*- coding: utf-8 -*-
#!/usr/bin/python

from django.shortcuts import render
from apps.blog.models import Article, Category, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.conf import settings


months = Article.objects.datetimes('pub_time', 'month', order='DESC')


category_list = Category.objects.all()  # select * from category ORDER BY `name` asc


tags = Tag.objects.all()  # 获取全部的标签对象 , select * from tag



def home(request):  # 主页
    posts = Article.objects.all()  # 获取全部的Article对象
    # select * from article limt <页数settings.PAGE_NUM >
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量，对应settings.py中的PAGE_NUM, 作为分页器处理
    page = request.GET.get('page')  # 获取URL中page参数的值
    try:
        # select * from article limit <pageSize> OFFSET  <page>
        post_list = paginator.page(page)  # 取第 page 页的数据 ,
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)  # 如果页码超出了当前数据量，显示最后一页
    return render(request, 'home.html', {
        'post_list': post_list,
        'category_list': category_list,
        'months': months,
    })


def detail(request, id):  # 查看文章详情
    try:
        # select * from article where `id` = 2
        post = Article.objects.get(id=str(id))
        post.viewed()   # 更新浏览次数
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {
        'post': post,
        'tags': tags,
        'category_list': category_list,

        'prev_post': post.prev_article(),  # model 定义的新方法
        'next_post': post.next_article(),
        'months': months,
    })



def category(request, id):
    # SELECT * FROM article WHERE category_id = 1
    # SELECT * FROM category WHERE id = 1
    posts = Article.objects.filter(category_id=str(id))  # 获取全部的Article对象
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量，对应settings.py中的PAGE_NUM, 作为分页器处理
    page = request.GET.get('page')  # 获取URL中page参数的值
    category_list = Category.objects.all()
    try:
        post_list = paginator.page(page)  # 取第 page 页的数据
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {
        'post_list': post_list,
        'category_list': category_list,
        'months': months,
    })


# 包含该tag 的文章列表
def tag(request, tag):
    # 先找到关联表 article_tags 中 article_tags.article_id = 3 的项， 保存这些项的 article_tags.tag_id, 再去tag 表查找符合  article_tags.tag_id 的项
    # SELECT * FROM `tag` INNER JOIN `article_tags` ON (`tag`.`id` = `article_tags`.`tag_id`) WHERE `article_tags`.`article_id` = 3
    posts = Article.objects.filter(tags__name__contains=tag)  # 获取全部的Article对象
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量，对应settings.py中的PAGE_NUM, 作为分页器处理
    page = request.GET.get('page')  # 获取URL中page参数的值
    category_list = Category.objects.all()
    try:
        post_list = paginator.page(page)  # 取第 page 页的数据
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {
        'post_list': post_list,
        'category_list': category_list,
        'months': months,
    })


#
def archives(request, year, month):
    posts = Article.objects.filter(pub_time__year=year, pub_time__month=month).order_by('-pub_time')
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量
    try:
        page = request.GET.get('page')  # 获取URL中page参数的值
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {
        'post_list': post_list,
        'category_list': category_list,
        'year_month': year+'年'+month+'月',
        'months': months,
        }
    )