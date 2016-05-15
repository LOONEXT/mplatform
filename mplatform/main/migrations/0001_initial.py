# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('tel', models.IntegerField(verbose_name='\u7535\u8bdd')),
                ('qq', models.IntegerField(verbose_name='QQ')),
                ('more', models.TextField(verbose_name='\u5907\u6ce8')),
                ('address', models.CharField(max_length=100, verbose_name='\u5730\u5740')),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u5ba2\u6237',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('tel', models.IntegerField(verbose_name='\u7535\u8bdd')),
                ('qq', models.IntegerField(verbose_name='QQ')),
                ('more', models.TextField(verbose_name='\u5907\u6ce8')),
                ('address', models.CharField(max_length=100, verbose_name='\u5730\u5740')),
                ('owner', models.ForeignKey(related_name='members', verbose_name='\u4e0a\u7ebf', blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u5458\u5de5',
            },
        ),
        migrations.CreateModel(
            name='PublicArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(verbose_name='\u7c7b\u578b', choices=[(1, '\u666e\u520a'), (2, '\u6838\u5fc3'), (3, '\u5b66\u62a5'), (4, '\u4e13\u5229'), (5, '\u5176\u4ed6')])),
                ('journal', models.CharField(max_length=100, verbose_name='\u520a\u7269')),
                ('periodical', models.CharField(max_length=20, verbose_name='\u671f\u6b21')),
                ('title', models.CharField(max_length=100, verbose_name='\u9898\u76ee')),
                ('totalmoney', models.FloatField(verbose_name='\u603b\u91d1\u989d')),
                ('deposit', models.FloatField(verbose_name='\u5b9a\u91d1')),
                ('rest', models.FloatField(verbose_name='\u4f59\u989d')),
                ('resttime', models.DateField(verbose_name='\u4f59\u989d\u5230\u6b3e\u65f6\u95f4')),
                ('bank', models.IntegerField(verbose_name='\u5230\u6b3e\u94f6\u884c', choices=[(1, '\u5efa\u884c'), (2, '\u5de5\u884c'), (3, '\u652f\u4ed8\u5b9d'), (4, '\u5fae\u4fe1')])),
                ('more', models.TextField(verbose_name='\u5458\u5de5\u5907\u6ce8')),
                ('status', models.IntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(1, '\u672a\u5b8c\u6210'), (2, '\u5b8c\u6210')])),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to='main.Client')),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u91c7\u7f16\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='WriteArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(verbose_name='\u7c7b\u578b', choices=[(1, '\u666e\u901a\u8bba\u6587'), (2, '\u7814\u7a76\u751f\u8bba\u6587'), (3, '\u6838\u5fc3'), (4, '\u5176\u4ed6')])),
                ('title', models.CharField(max_length=100, verbose_name='\u9898\u76ee')),
                ('wordcount', models.IntegerField(verbose_name='\u5b57\u6570')),
                ('perword', models.FloatField(verbose_name='\u5355\u4ef7\uff08\u5343\u5b57\uff09')),
                ('totalmoney', models.FloatField(verbose_name='\u603b\u91d1\u989d')),
                ('deposit', models.FloatField(verbose_name='\u5b9a\u91d1')),
                ('rest', models.FloatField(verbose_name='\u4f59\u989d')),
                ('finishtime', models.DateField(verbose_name='\u4ea4\u7a3f\u65f6\u95f4')),
                ('bank', models.IntegerField(verbose_name='\u5230\u6b3e\u94f6\u884c', choices=[(1, '\u5efa\u884c'), (2, '\u5de5\u884c'), (3, '\u652f\u4ed8\u5b9d'), (4, '\u5fae\u4fe1')])),
                ('more', models.TextField(verbose_name='\u5458\u5de5\u5907\u6ce8')),
                ('status', models.IntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(1, '\u672a\u5b8c\u6210'), (2, '\u4fee\u6539\u4e2d'), (3, '\u5b8c\u6210'), (4, '\u9ec4\u7a3f')])),
                ('client', models.ForeignKey(verbose_name='\u4e0b\u5355\u4eba', to='main.Client')),
                ('owner', models.ForeignKey(verbose_name='\u63a5\u5355\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u91c7\u7f16\u4fe1\u606f',
            },
        ),
    ]
