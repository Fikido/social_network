# Generated by Django 3.0 on 2020-02-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0035_auto_20200214_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='biography',
            field=models.TextField(blank=True),
        ),
    ]
