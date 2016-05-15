# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160515_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='owner',
            field=models.ForeignKey(related_name='members', verbose_name='\u4e0a\u7ebf', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
