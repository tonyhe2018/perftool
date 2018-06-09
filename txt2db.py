#!/usr/bin/python3
#coding:utf-8

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

if django.VERSION >=(1,7):
    django.setup()

def main():
    from blog.models import Blog
    f = open('/home/myproject/blog/log_file/oldblog.txt')
    #for line in f.readlines():
    #    title,content = line.split('****')
    #    print(title,content)
    #    Blog.objects.create(title = title, content = content)
    #f.close()
    #blog_list = list()
   # for line in f:
    #    a, b = line.split('****')
    #    blog_list.append(Blog(title = a, content = b))
    #f.close()
    #Blog.objects.bulk_create(blog_list)
    blog_dict = dict()
    for line in f.readlines():
        a, b = line.split('****')
        print('a===',a,type(a),'======b====',b,type(b))
        try:
            type(blog_dict[line]) == dict
        except:
            blog_dict[line] = dict()
        finally:
            blog_dict[line] = {'title' : a.split(' ')[1], 'content' : b.split(' ')[1]}

    print(blog_dict)
    for key,value in blog_dict.items():
        Blog.objects.create(title = value['title'], content = value['content'])

    Blog.objects.all()
  
if __name__ == '__main__':
    main()
    print('Done')
