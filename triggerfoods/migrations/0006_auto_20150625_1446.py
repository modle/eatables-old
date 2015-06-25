# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triggerfoods', '0005_auto_20150625_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='triggerfood',
            options={'ordering': ('-severity', 'name')},
        ),
    ]
