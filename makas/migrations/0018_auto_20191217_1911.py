# Generated by Django 3.0 on 2019-12-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0017_auto_20191217_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='attachments',
            field=models.FileField(default='', upload_to='post/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PostAttachments',
        ),
    ]
