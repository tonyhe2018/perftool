# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('pub_data', models.DateTimeField(auto_now_add=True, verbose_name='publish date')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='update date')),
            ],
        ),
    ]