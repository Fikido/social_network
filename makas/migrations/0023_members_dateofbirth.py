# Generated by Django 3.0 on 2020-02-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0022_auto_20191222_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='dateofbirth',
            field=models.CharField(default='', max_length=100),
        ),
    ]
