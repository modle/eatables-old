# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triggerfoods', '0002_triggerfood_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triggerfood',
            name='severity',
            field=models.IntegerField(max_length=1),
        ),
    ]
