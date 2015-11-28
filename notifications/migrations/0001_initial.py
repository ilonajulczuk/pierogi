# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('device_token', models.CharField(max_length=64, db_index=True, help_text='Device token used for notifications')),
                ('device_type', models.CharField(max_length=32)),
                ('first_registered_at', models.DateTimeField(auto_now_add=True, help_text='Date and time when the device was first registered')),
                ('last_login_at', models.DateTimeField(auto_now=True, help_text='Date and time when the device was last used to log in')),
                ('is_active', models.BooleanField(default=True, help_text='If checked, the device will receive notifications')),
                ('user', models.ForeignKey(related_name='devices', help_text='Employee that last logged in using this device', to=settings.AUTH_USER_MODEL, verbose_name='Last used by')),
            ],
        ),
    ]
