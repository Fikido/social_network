# Generated by Django 3.0 on 2019-12-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makas', '0012_auto_20191217_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAttachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='post/attachments')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='attachements',
            field=models.ManyToManyField(to='makas.PostAttachments'),
        ),
    ]