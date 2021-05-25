# Generated by Django 3.2.3 on 2021-05-21 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='comments',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='detail',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 21, 23, 32, 22, 545409)),
        ),
        migrations.AddField(
            model_name='detail',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='detail',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='detail',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
