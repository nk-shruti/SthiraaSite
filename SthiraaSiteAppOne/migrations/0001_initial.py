# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('aid', models.AutoField(serialize=False, primary_key=True)),
                ('heading', models.CharField(default=b'', max_length=800, blank=True)),
                ('author', models.CharField(default=b'', max_length=200, blank=True)),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to=None)),
                ('content', models.FileField(upload_to=b'documents/')),
            ],
        ),
    ]
