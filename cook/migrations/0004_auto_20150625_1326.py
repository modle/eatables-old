# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0003_triggerfoods'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TriggerFoods',
            new_name='TriggerFood',
        ),
    ]
