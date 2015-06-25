# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0002_recipe_directions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TriggerFoods',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('severity', models.CharField(max_length=10)),
            ],
        ),
    ]
