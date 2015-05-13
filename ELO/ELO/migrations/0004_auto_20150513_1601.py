# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ELO', '0003_god'),
    ]

    operations = [
        migrations.RenameField(
            model_name='god',
            old_name='value',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='god',
            old_name='field',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='god',
            name='identity',
        ),
    ]
