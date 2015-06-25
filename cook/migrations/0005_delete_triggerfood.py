# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0004_auto_20150625_1326'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TriggerFood',
        ),
    ]
