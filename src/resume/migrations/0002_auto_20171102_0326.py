# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Is this experience public?'),
        ),
        migrations.AlterField(
            model_name='workexperiencetranslation',
            name='language',
            field=models.CharField(choices=[('en-us', 'English'), ('zh-hans', 'Chinese')], db_index=True, max_length=30, verbose_name='Language'),
        ),
    ]
