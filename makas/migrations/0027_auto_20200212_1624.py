# Generated by Django 3.0 on 2020-02-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0026_auto_20200212_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='attachment',
            field=models.FileField(upload_to='post/'),
        ),
    ]
