# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=3, choices=[('LEV', 'LEVESEK'), ('FO', 'FŐÉTELEK'), ('ED', 'ÉDESSÉGEK'), ('SO', 'SÓSAK')]),
        ),
    ]
