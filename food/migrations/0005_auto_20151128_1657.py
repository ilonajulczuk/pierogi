# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20151128_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='taker',
            field=models.ForeignKey(null=True, related_name='food_taken', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
