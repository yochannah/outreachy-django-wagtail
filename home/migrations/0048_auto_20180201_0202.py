# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20180201_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantapproval',
            name='other_time_commitments',
            field=models.TextField(blank=True, help_text='(Optional) If you have other time commitments outside of school, work, or volunteer hours, please use this field to let your mentor know. Examples of other time commitments include vacation that lasts longer than a week, coding school time commitments, community or online classes, etc.', max_length=3000),
        ),
    ]
