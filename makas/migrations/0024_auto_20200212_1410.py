# Generated by Django 3.0 on 2020-02-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0023_members_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='users/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='members',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
