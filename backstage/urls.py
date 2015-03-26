# !/usr/bin/env python
# coding:UTF-8
# Created Time:2015-03-24
# Auther dub
from django.conf.urls import patterns, include, url

from backstage import views
urlpatterns = patterns('',
    url(r'^$', views.index ,name='upload'),
)
