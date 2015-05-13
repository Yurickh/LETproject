# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ELO', '0002_delete_god'),
    ]

    operations = [
        migrations.CreateModel(
            name='God',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identity', models.IntegerField()),
                ('field', models.CharField(max_length=32)),
                ('value', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
