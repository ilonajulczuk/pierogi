# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('name', models.CharField(max_length=255, blank=True, null=True, default=None)),
                ('should_be_notified', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('giver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='food_given')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('company', models.ForeignKey(to='food.Company')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='place',
            field=models.ForeignKey(to='food.Place'),
        ),
        migrations.AddField(
            model_name='food',
            name='taker',
            field=models.ForeignKey(related_name='food_taken', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='fooduser',
            name='company',
            field=models.ForeignKey(to='food.Company'),
        ),
    ]
