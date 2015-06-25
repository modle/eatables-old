# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triggerfoods', '0003_auto_20150625_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triggerfood',
            name='severity',
            field=models.IntegerField(),
        ),
    ]
