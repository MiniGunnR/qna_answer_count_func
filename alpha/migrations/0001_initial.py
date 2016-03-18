# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('answers', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alpha.Question'),
        ),
    ]
