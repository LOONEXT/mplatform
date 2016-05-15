# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='owner',
            field=models.ForeignKey(related_name='members', verbose_name='\u4e0a\u7ebf', blank=True, to='main.Employee', null=True),
        ),
    ]
