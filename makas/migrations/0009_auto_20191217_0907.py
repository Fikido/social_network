# Generated by Django 3.0 on 2019-12-17 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0008_posts_posttitme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='posttitme',
            field=models.TimeField(auto_now=datetime.time),
        ),
    ]
