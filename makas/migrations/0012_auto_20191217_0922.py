# Generated by Django 3.0 on 2019-12-17 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0011_auto_20191217_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='posttitme',
            new_name='posttime',
        ),
    ]
