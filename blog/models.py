#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField('title', max_length = 50)
    content = models.TextField('content')
    pub_data = models.DateTimeField('publish date', auto_now_add = True, editable = True)
    update_time = models.DateTimeField('update date', auto_now = True, null = True)

    def __str__(self):
        return self.title
