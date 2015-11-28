# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20151128_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='giver',
            field=models.ForeignKey(blank=True, related_name='food_given', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
