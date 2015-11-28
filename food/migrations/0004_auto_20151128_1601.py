# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20151128_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='place',
            field=models.ForeignKey(null=True, blank=True, to='food.Place'),
        ),
    ]
